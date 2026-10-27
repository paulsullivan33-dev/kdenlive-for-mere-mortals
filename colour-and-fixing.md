# Colour and Fixing Shaky Footage

By the end of this chapter you can rescue
footage that is too dark, too blue, or
too wobbly — honestly, which means you
will also know what cannot be rescued,
and you will check your fixes on
instruments instead of trusting a screen
in a sunlit room. This chapter is
documented-only in the lab's ledger: the
fixes are window work and the build
machine has no window, so the guide
describes Kdenlive's documented behaviour
and leans on chapter 2's scopes — while
the file-level truth underneath (effects
are instructions, chapter 8) is the part
the lab did verify.

## Fix in the right order

Colour work has a traditional order, and
skipping steps is how fixes fight each
other:

1. **Exposure** — is it the right
   brightness overall?
2. **White balance** — are the whites
   actually white, or tinted?
3. **Contrast and saturation** — does it
   look alive, neither washed nor garish?

Kdenlive's tools for these live in the
effects list under colour correction:
**Brightness**, **Contrast**,
**Saturation**, **White Balance**,
**Levels** and **Curves** for finer
hands. Apply them to the clip, judge on
the scopes, compare with the effect
ticked off (chapter 8's discipline).

## Reading the scopes

The **waveform** draws the picture's
brightness as a landscape: height is
brightness, left-to-right matches the
picture. Two readings matter most. If
nothing in the waveform reaches the top,
the shot is dull and can be lifted. If
the landscape is crushed flat against
the top or bottom, detail there is
*clipped* — recorded as pure white or
pure black — and no slider brings detail
back, because it was never recorded
(chapter 15's theme, arriving early).

The **histogram** counts tones instead
of placing them; the **vectorscope**
draws colour as direction and distance
from centre, which is how you see a
tint: whites that should sit in the
middle sit off to one side, and white
balance is the act of walking them home.

## Too dark, too blue, in practice

- **Too dark:** raise Brightness a
  little, then Levels or Curves to lift
  the middle tones (the **gamma**) more
  than the blacks. Dark footage raised
  too far shows **noise** — coloured
  speckle in the shadows, the sensor's
  struggle made visible. Some noise is
  the honest price of the rescue.
- **Too blue (or orange):** White Balance
  asks you to point at something that
  should be neutral — a wall, a shirt, a
  sheet of paper in shot — and it shifts
  the whole palette so that thing is.
  No neutral object? The temperature
  slider by eye, checked on the
  vectorscope, is the fallback.
- **Flat and grey** (common with log-style
  camera settings and dull days): a
  gentle S in Curves — shadows a touch
  darker, highlights a touch brighter —
  and saturation up a few points.

Fix the *worst* clip to look right, then
copy its effect stack to its neighbours
(right-click → copy, paste effects) and
adjust. A film whose shots differ wildly
in colour reads as several films.

## Shaky footage

Kdenlive's answer is a **clip job**:
right-click the clip in the bin →
Clip Jobs → **Stabilize**. It analyses
the shot in a separate pass (the
vid.stab library underneath), writes its
measurements beside the clip, and the
stabilised version becomes a new clip
that *crops in* slightly — stabilising
works by moving the frame opposite the
shake, so the edges need material to
spare, and the more violent the shake,
the deeper the crop and the softer the
picture.

What it does well: walking shots smoothed
to a glide, handheld tremble calmed, a
tripod bump removed. What it cannot do:
rescue shots where the shake is mixed
with motion blur (each frame is a smear;
there is nothing to align), rolling
shutter wobble from cheap sensors (the
"jello" bend in pans), or a subject who
leaves the frame. Set expectations by
the original sin: the steadier the
recording, the lighter the fix. A
stabilised clip also costs render time
and a generation of re-encoding before
it ever reaches the timeline.

Check: take your worst-lit clip, fix it
in the order above until the waveform
fills its range without crushing either
end, and compare ticked on and off. Then
stabilise the shakiest ten seconds you
own and watch the edges: the crop you
see is the shake you had, made visible.
