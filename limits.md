# Limits

An honest chapter, and a short one
because the tool is honest: Kdenlive
does a wide job well, and its edges are
knowable in advance. Everything here is
a property of the tool or of the
footage, not a failure of the reader.

## It cannot invent what was not recorded

The hardest limits are physics wearing a
software coat. Highlights or shadows
**clipped** to pure white or black hold
no detail to recover (chapter 9).
Footage blurred by motion is a smear in
every frame; sharpening makes a crisper
smear. Stabilising (chapter 9) trades
picture area for smoothness and bows out
entirely against rolling-shutter wobble.
Low light means **noise**, and removing
noise removes fine detail in the same
pass. In every case the fix is at the
recording, and the editor's job is to
make the best of what arrived.

## Variable frame rate will fight you

Phones and screen recorders often record
**variable frame rate** (VFR) footage:
the spacing between frames changes with
the scene. Timelines think in fixed
frames, and VFR shoehorned into one can
drift — most famously, sound sliding out
of step with picture over a long clip.
Kdenlive warns about VFR on import and
offers to **transcode** it to a constant
rate; accepting is the fix, and it is a
re-encode of the whole clip before you
begin. This guide's advice is blunt:
transcode phone footage first, edit
second.

## Speed is a budget, and effects spend it

The engine renders effects on the CPU in
the general case. A timeline of plain
cuts previews and renders quickly; every
stacked effect — colour, blur, transform,
stabilised footage — multiplies the work
per frame, and a render can run many
times slower than the film's length.
Proxies (chapter 12) relieve *editing*,
not rendering. GPU processing (Movit)
can help where it works and is the first
suspect where previews misbehave
(chapter 16); this guide's standing
advice is to leave it off unless a
measured need says otherwise.

## One editor, one file, no cloud

A Kdenlive project is one file edited by
one person at a time. There is no live
collaboration, no comment threads, no
version history beyond the copies you
save yourself, and the project format —
MLT XML, chapter 11 — ties the project
to the MLT family of tools. Archive
(chapter 11) is the portability story,
and it is a good one; a shared, live,
multi-author document is a different
kind of tool, and this is not it.

## Sound stops at the studio door

Chapter 6's tools — levels, fades,
normalising, the mixer, a shelf of audio
effects — cover editing sound. They do
not make Kdenlive a recording studio:
there is no spectral repair (painting
out one noise from a spectrogram), no
multi-track recording session workflow,
and noise reduction is a blunt effect,
not an restoration lab. Films whose
sound needs surgery deserve a dedicated
audio tool, and a related guide covers
one (Audacity).

## The preview is a promise, not the film

The project monitor shows the engine's
intent at preview quality, with proxies
if you use them, under your room's
light. The render is the film. Colour
can shift a step between them (preview
shortcuts, a player's levels
interpretation, an upload site's
re-encode), which is why chapters 4 and
10 both end the same way: judge the
rendered file, in a player, every time.
