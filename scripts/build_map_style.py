"""Build a walking-scale basemap with a street / block / landmark hierarchy.

Uses the saved OpenFreeMap Positron source and OpenMapTiles schema.
All geometry and context labels come from the vector tiles, never invented POIs.
"""
from copy import deepcopy
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
base = json.loads((root / 'scripts/openfreemap-positron.json').read_text(encoding='utf-8-sig'))
source = deepcopy(base['sources']['openmaptiles'])
source['attribution'] = '<a href="https://openfreemap.org/">OpenFreeMap</a> · © <a href="https://openmaptiles.org/">OpenMapTiles</a> · © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> · <a href="maps/credits.html" target="_blank" rel="noopener">스타일 출처</a>'
name = ['coalesce', ['get', 'name:ko'], ['get', 'name:nonlatin'], ['get', 'name'], ['get', 'name:latin'], '']
layers = []

def ramp(*stops):
    return ['interpolate', ['linear'], ['zoom'], *stops]

def match_class(values):
    return ['match', ['get', 'class'], values, True, False]

def add(key, kind, source_layer=None, paint=None, layout=None, filter=None, minzoom=None, maxzoom=None):
    layer = {'id': key, 'type': kind}
    if source_layer:
        layer.update({'source': 'openmaptiles', 'source-layer': source_layer})
    if paint: layer['paint'] = paint
    if layout: layer['layout'] = layout
    if filter: layer['filter'] = filter
    if minzoom is not None: layer['minzoom'] = minzoom
    if maxzoom is not None: layer['maxzoom'] = maxzoom
    layers.append(layer)

add('background', 'background', paint={'background-color': '#ffffff'})
add('park', 'fill', 'park', {'fill-color': '#efede5'}, filter=['==', ['geometry-type'], 'Polygon'])
add('wood', 'fill', 'landcover', {'fill-color': '#f0eee7', 'fill-opacity': .8},
    filter=match_class(['wood', 'grass']), minzoom=11)
add('water', 'fill', 'water', {'fill-color': '#e2e5e5'}, filter=['!=', ['get', 'brunnel'], 'tunnel'])
add('buildings', 'fill', 'building',
    {'fill-color': '#e9e6df', 'fill-opacity': ramp(14, .25, 15, .65, 16, .9)}, minzoom=14)

line_layout = {'line-cap': 'round', 'line-join': 'round'}
add('waterway', 'line', 'waterway', {'line-color': '#c8cdcd', 'line-width': ramp(13, 1, 18, 2)}, minzoom=13)
add('walking-paths', 'line', 'transportation',
    {'line-color': '#bcb5a7', 'line-width': ramp(16, .9, 18, 1.8, 20, 2.8),
     'line-dasharray': [1.5, 2], 'line-opacity': .8}, line_layout,
    match_class(['path', 'track']), minzoom=16)

def road(key, classes, outer, inner, edge, minzoom):
    rule = match_class(classes)
    add(f'{key}-edge', 'line', 'transportation', {'line-color': edge, 'line-width': outer}, line_layout, rule, minzoom)
    add(f'{key}-surface', 'line', 'transportation', {'line-color': '#ffffff', 'line-width': inner}, line_layout, rule, minzoom)

# White road corridors distinguish streets from solid building footprints.
road('service', ['service'], ramp(16, 2, 18, 5.5, 20, 10), ramp(16, 1, 18, 4, 20, 8.5), '#e1dcd2', 16)
road('local', ['minor'], ramp(13, 1.5, 15, 4, 17, 7, 19, 12), ramp(13, .5, 15, 2.5, 17, 5.5, 19, 10.5), '#d9d3c8', 13)
road('connector', ['tertiary', 'secondary'], ramp(12, 2.5, 15, 7, 17, 12, 19, 22), ramp(12, 1.2, 15, 5, 17, 10, 19, 20), '#c9c2b5', 12)
road('arterial', ['primary', 'trunk', 'motorway'], ramp(11, 3, 14, 7, 16, 13, 18, 23, 20, 40), ramp(11, 1.5, 14, 5, 16, 11, 18, 21, 20, 38), '#bdb5a6', 11)

def labels(key, source_layer, rule, size, color, minzoom, bold=False, extra=None):
    layout = {'text-field': name, 'text-font': ['Noto Sans Bold' if bold else 'Noto Sans Regular'],
              'text-size': size, 'text-padding': 6, 'text-letter-spacing': 0, 'text-max-width': 10}
    if extra: layout.update(extra)
    add(key, 'symbol', source_layer,
        {'text-color': color, 'text-halo-color': '#ffffff', 'text-halo-width': 1.7, 'text-halo-blur': 0},
        layout, rule, minzoom)

labels('local-road-names', 'transportation_name', match_class(['minor', 'tertiary']),
       ramp(16, 12, 18, 13.5), '#777064', 16,
       extra={'symbol-placement': 'line', 'symbol-spacing': 400, 'text-max-angle': 30})
labels('main-road-names', 'transportation_name', match_class(['primary', 'secondary', 'trunk']),
       ramp(13, 13, 16, 14, 18, 15), '#5e584d', 13,
       extra={'symbol-placement': 'line', 'symbol-spacing': 450, 'text-max-angle': 30})
labels('neighborhoods', 'place',
       ['match', name, ['북촌', '서촌', '계동', '안국동', '옥인동', '통인동'], True, False],
       13, '#827b6e', 13)

# A few orientation landmarks, not every commercial POI. Tile geometry only.
landmarks = ['경복궁', '창덕궁', '광화문', '광화문광장', '사직공원', '사직단',
             '국립현대미술관 서울', '국립현대미술관 서울관', '청와대', '종묘', '인왕산']
landmark_filter = ['match', name, landmarks, True, False]
labels('landmarks', 'poi', landmark_filter, ramp(13, 14, 16, 16), '#696252', 13, bold=True)
labels('park-names', 'park', ['all', ['==', ['geometry-type'], 'Point'], landmark_filter],
       15, '#696252', 13, bold=True)
station_filter = ['all', ['==', ['get', 'class'], 'railway'],
                  ['match', ['get', 'subclass'], ['station', 'subway', 'halt'], True, False]]
add('station-points', 'circle', 'poi',
    {'circle-radius': 4, 'circle-color': '#6d685f', 'circle-stroke-color': '#ffffff', 'circle-stroke-width': 2},
    filter=station_filter, minzoom=12)
labels('stations', 'poi', station_filter, 14, '#444037', 12, bold=True,
       extra={'text-field': ['case', ['in', '역', name], name, ['concat', name, '역']],
              'text-anchor': 'top', 'text-offset': [0, .65], 'text-padding': 14})

style = {'version': 8, 'name': 'Alley — streets, blocks and landmarks',
         'sources': {'openmaptiles': source}, 'glyphs': base['glyphs'], 'layers': layers}
target = root / 'maps/alley-style.json'
target.write_text(json.dumps(style, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Wrote {len(layers)} map layers to {target.name}')
