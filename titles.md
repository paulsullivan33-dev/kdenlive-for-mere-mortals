# Titles

By the end of this chapter you can put
words on the film — an opening title, a
name under a speaker, a closing credit —
and know where those words live in the
project, because titles are the one part
of a film this guide's lab could build
and verify entirely from the file.

## A title is a clip

In Kdenlive, text is not typed onto the
video. You make a **title clip** in the
bin (Add Title Clip), design it in the
**title window**, and place it on the
timeline like any clip — on a video track
above the picture, for exactly as long as
it should stay on screen. Its beginning
and end are trimmed like any clip's
(chapter 5), and a fade is chapter 8's
trick: a transparency or brightness
keyframe walk at its edges.

The title window gives you a canvas the
size of the project frame, text items you
can add and restyle (font, size, colour,
outline, shadow), rectangles and images,
and alignment tools. The centre of the
canvas is marked with the **title-safe
area** — a frame inside the frame; words
kept inside it survive televisions and
players that crop edges. Keep titles
short, large, and on screen longer than
feels necessary: a viewer reads at half
the speed you wrote.

The everyday titles are three:

- **Opening title** — the film's name,
  over the first shot or over black.
- **Lower third** — the small name-and-role
  strip near the bottom that introduces a
  speaker ("Ana Ruiz, head gardener").
- **Credits** — the closing list; a
  title clip held for a few seconds is
  kinder than a scroll nobody can read.

## What a title is, in the file

A title clip's design is a small XML
document in Kdenlive's own title format,
and the timeline references it as a clip
whose engine service is `kdenlivetitle`.
The lab's title, copied from a template
Kdenlive itself ships, reads:

```xml
<kdenlivetitle width="1280" height="720" out="49">
 <item z-index="0" type="QGraphicsTextItem">
  <position x="215" y="308">...</position>
  <content font-color="255,255,255,255"
           font-pixel-size="76"
           font="DejaVu Sans">A Short Garden Tour</content>
 </item>
 <background color="0,0,0,0"/>
</kdenlivetitle>
```

Note the background: fully transparent.
That is why the title track must sit
*above* the picture track, and why the
text appears over the film rather than
replacing it. In the lab's render the
title stands over the first clip for its
fifty frames and is gone by frame 50 —
verified from stills of the rendered
file, not from hope (`kdenlive-lab/
transcripts/t03`).

## The headless trap, once

Titles are drawn by the same Qt machinery
that draws Kdenlive's window. On a machine
(or a render script) with no display, the
title cannot be drawn, and the engine
substitutes a placeholder: the word
INVALID in enormous letters across the
frame. The lab met it, diagnosed it
(chapter 16), and fixed it by rendering
under a fake display. On a desktop with
Kdenlive open you will never see it — but
if a *rendered file* ever shows INVALID
where your title should be, you now know
more than the error message tells you.

Check: put a lower third under a speaker
(or over any clip): your name, one line,
inside the safe area, on the track above
the picture, held for four seconds, with
a half-second fade at both ends. Render
ten seconds and read the title in the
player — if you can read it comfortably
at arm's length, it is big enough.
