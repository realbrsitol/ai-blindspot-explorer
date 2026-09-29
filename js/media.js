// Derived previews preserve the full photo. Keep the credited original as a fallback.
window.AlleyMedia = {
  create(place, { detail = false, eager = false, onLoad, onError } = {}) {
    const image = document.createElement('img');
    image.alt = place.imageAlt;
    image.loading = eager ? 'eager' : 'lazy';
    image.decoding = 'async';
    image.addEventListener('load', () => onLoad?.());
    let usingOriginal = false;
    image.addEventListener('error', () => {
      if (usingOriginal) { onError?.(); return; }
      usingOriginal = true;
      image.removeAttribute('srcset');
      image.src = place.image;
    });
    image.src = detail ? place.largePreview : place.preview;
    return image;
  }
};
