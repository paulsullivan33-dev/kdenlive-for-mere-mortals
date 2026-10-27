# The Moving Parts

Kdenlive's window has more panels than a
first look suggests. Knowing which part
holds what is the difference between "the
editor is broken" and "that clip is on
the wrong track" — a distinction this
guide leans on constantly. By the end of
this chapter you can name every part and
say what it is for.

## The project bin

The **bin** is the shelf where a
project's raw material lives: every video
clip, sound file, picture and title you
have added, listed with its length and
size. Nothing in the bin is in the film
yet. Deleting something from the bin does
not delete the file from your disk — the
bin holds *references*, paths to files,
not the files themselves. Chapter 11 is
about what follows from that, and it is
the single most useful fact in this
guide.

## The monitors

Two small televisions sit at the top of
the window. The **clip monitor** shows
one bin clip at a time, for auditioning:
play it, mark the good stretch with an
**in point** and an **out point** (the
keys I and O), and only that stretch need
ever reach the timeline. The **project
monitor** shows the film itself — the
timeline as it will render, playhead and
all. If you are ever unsure which one you
are looking at, the project monitor is
the one that shows titles and edits; the
clip monitor only ever shows one raw
clip, untouched.

## The timeline

The **timeline** is where the film is
built: a set of horizontal **tracks**
running left to right, with time along
the top. Video tracks stack — a clip on a
higher track covers whatever is beneath
it for as long as it lasts, which is how
titles sit on top of pictures. Audio
tracks simply add: every audible track
sounds at once, mixed. A **playhead**
marks the current moment, and dragging
clips along a track, or trimming their
ends, is most of editing (chapter 5).

Two facts about tracks repay learning
early. First, the stack has a top and the
top wins: a title that "isn't showing" is
usually a title placed *under* the video
it should cover. Second, each track can
be hidden, muted, or locked with the
small icons at its left end — a locked
track cannot be changed by accident,
which is the state finished tracks
deserve.

## Effects and the effect stack

An **effect** is an instruction attached
to a clip (or a track): *brighten this*,
*make this quieter*, *fade this out*.
Effects accumulate in an **effect stack**,
shown when a clip is selected, and they
apply in order, top to bottom. Most
effects have **keyframes** — marks saying
"the value is this here, and that later"
— so a value can change over time: a fade
is nothing more than a brightness or
volume effect whose keyframes walk from
nothing to full. Chapters 6, 8 and 9 are
built on that one idea.

## Sound's furniture

Audio has its own furniture beyond the
timeline: an **audio mixer** with a fader
and a level meter per track, and meters
that show how loud the mix is moment by
moment. Sound is measured in **decibels**
(dB), where 0 dB is the loudest a digital
file can be and everything real lives
below it. Chapter 6 works there.

## The scopes

Under the View menu live the **scopes**:
instruments that draw the picture's
brightness and colour as graphs — a
histogram, a waveform, a vectorscope.
They are how you fix colour with evidence
instead of by eye alone (chapter 9), and
they read the same numbers no matter how
the room is lit, which your eyes do not.

## The rendering dialog

The last part is a door out: the
**rendering dialog** (the Render button),
where you pick a **preset** — a named
bundle of format choices, like "MP4" —
and start the render. What comes out is a
new, ordinary video file. Chapter 10
covers the choices; chapter 11 covers
what stays behind (the project), because
the two are constantly confused.

## Who holds what, when it breaks

- The **bin** holds paths, not media. A
  moved file is a missing clip (chapter
  16's checkerboard).
- The **timeline** holds the arrangement;
  the **project file** holds the timeline.
- **Effects** hold the dressing; remove
  one and the clip underneath is the raw
  clip again, untouched.
- The **render** holds nothing back: it
  is the only place the film exists as a
  film, which is why you always check the
  render, never just the timeline.
