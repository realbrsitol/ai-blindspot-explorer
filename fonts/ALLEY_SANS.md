# Alley Sans

The app uses **Alley Sans**, a local character subset derived from the included
Pretendard Variable font by Kil Hyung-jin. It preserves the original outlines
and variable weight axis. The derivative is renamed because **Pretendard** is
a Reserved Font Name under the SIL Open Font License 1.1.

The original font and its license remain in this directory. Alley Sans is also
distributed under the SIL Open Font License 1.1. The copyright and license
records embedded in the font are preserved.

Run `python scripts/build_preview_assets.py` from the repository after changing
UI copy. The subset covers application copy, basic Latin and Korean compatibility
jamo. Other text uses the device's system font; loading a map never requires the
full original font. This is a byte-size optimization, not a different type design.

Since v24, Japanese uses the device's Japanese sans-serif stack, and Simplified
Chinese uses its Chinese sans-serif stack. These translations are not added to
the Korean/Latin subset. No additional remote font request is required.
