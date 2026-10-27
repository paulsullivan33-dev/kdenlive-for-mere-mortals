# What Kdenlive Is

You have video clips. They are too long,
they start too late, the interesting part
is in the middle, and one of them has the
sound of a washing machine over the whole
thing. **Kdenlive** is the program that
turns those clips into a film: you lay
them end to end on a **timeline**, cut
away the parts you do not want, put words
and sound over the top, and **render** —
the program's word for building the
finished video file you can share.

Kdenlive is a **non-linear editor**. The
name means you are not forced to work
from the start of the film to the end, in
order, the way tape editing once worked.
Any clip can be moved, trimmed, or cut at
any time, in any order, and nothing is
final until you render. The original
clips are never changed: Kdenlive keeps a
list of instructions — *play this file
from second 4 to second 9, then that
file, with these words on top* — and the
render is where those instructions are
carried out. Chapter 11 shows the
instruction list itself; it is a text
file you can read.

Kdenlive is free and open source, made by
the KDE community, and runs on Linux,
Windows and macOS. Underneath it sits a
media engine called **MLT**, which does
the actual decoding, mixing and encoding;
Kdenlive is the workbench built on top of
that engine. That division matters twice
in this guide: the project file is MLT's
file format (chapter 11), and the lab
behind this guide could test renders with
MLT's own renderer, **melt**, on a machine
with no screen — the same engine, driven
from the command line.

## The one rule, stated early

An editor makes copying and rearranging
other people's work easy. So this guide
has one rule, and it is not fine print:

> **Edit footage you made yourself, or
> footage you have clear permission to
> use — and treat music the same way.**

Your own holiday clips, your club's own
recordings with the club's agreement,
footage a client handed you for the job:
yes. A film you downloaded, a song from a
streaming service laid under your video
because it fits: no — the fact that the
editor *can* place it on the timeline
says nothing about whether you may
publish the result. The lab in this guide
went further than most readers will need
to: its film is six seconds of coloured
rectangles and a tone, invented for the
occasion, so nobody's footage appears
anywhere in it but the lab's own.

## Who it is for

The person with a folder of phone clips
who wants one watchable film out of them.
The club secretary recording talks. The
teacher assembling a demo from screen
recordings and a commentary track. The
common thread is one person, their own
footage, and a film that needs cuts,
order, words and sound more than it needs
cinema glamour.

## What it is not

Kdenlive is not a camera and not a
recorder: capturing is a different job
(OBS Studio's country, and a related
guide covers it). It is not a finishing
suite for cinema colour work — chapter 9
covers honest colour fixing, and chapter
15 is plain about where that ends. It is
not a media player with trim buttons; if
all you want is the middle ten seconds of
one clip, chapter 14 shows a one-line
tool that does exactly that and nothing
more. And it is not magic: it cannot make
footage sharp that was recorded blurry,
or steady footage that was never steady —
chapter 9 explains what fixing can and
cannot recover.

## A first taste of the shape

Every project in this guide follows the
same arc, and the chapters follow it too:

1. **Gather** clips into the project's
   **bin** — its shelf of raw material.
2. **Arrange** them on the timeline,
   cutting and trimming as you go.
3. **Dress** the result: titles, sound,
   fades, small fixes.
4. **Render** one finished file, and
   check it by playing it.

Check: if that four-step shape makes
sense, chapter 2's map of the parts will
too — every part exists to serve one of
those steps.
