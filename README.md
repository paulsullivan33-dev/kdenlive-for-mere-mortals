# Kdenlive for Mere Mortals

A camera gives you clips: too long, in
the wrong order, starting ten seconds
before anything happens. **Kdenlive**
is the free editor that turns clips
into a film — you lay them on a
**timeline**, cut what does not belong,
put titles and sound over the top, fix
what can be fixed, and **render** one
finished file to share. It is a
**non-linear editor**: nothing is final
until the render, and the original
clips are never touched.

This guide explains how that works:
what the parts of the window hold, how
a first project goes from empty folder
to finished film, how cutting, sound,
titles, effects and colour fixing
actually work, what a render really is,
and why a project file is a few
kilobytes of text pointing at gigabytes
of other people's bytes. The limits are
stated plainly, including the one that
matters most in practice: an editor can
only work with what was recorded.

The rule that governs everything here
is stated in chapter 1 and repeated
where it bites: **your footage, or
footage you have clear permission to
use — and music counts as footage.**
The lab obeyed it strictly. Its film is
six seconds long and was invented for
the occasion: two coloured rectangles
with labels, a tone for sound, and a
title, so that every frame of evidence
in this guide is the lab's own.

The lab behind this guide ran the real
thing where a screenless machine
allows: **Kdenlive 23.08.5** and
**melt 7.22.0** — the MLT renderer
Kdenlive renders through — installed
with apt on a small Linux machine. The
lab wrote a minimal project in
Kdenlive's own file format (a real
`.kdenlive` text file, kept in the
repository), rendered it to MP4 and to
WebM, and read the results back with
ffprobe: streams, sizes, exact frame
counts. It measured the fades it had
written into the file — frame
brightness climbing across a
fade-from-black, sound level climbing
across a fade-in — watched a title clip
composite over the picture, broke a
media path on purpose and rendered the
grey checkerboard that replaced the
missing clip, and timed a 4K clip
against its own proxy to show what
proxies are for.

What the lab could not do, it did not
fake. The build machine has no display,
so everything done with a mouse in the
editing window — dragging clips,
razor work, designing titles, judging
colour — is taught from Kdenlive's
documentation and labelled as such in
`criteria.md`, which keeps the full
ledger. What the lab *did* verify is
the layer underneath the window: the
project file's contents, the engine's
renders, and the numbers those renders
obey. Where the two meet — a fade in
the file is the same fade the window
draws — the guide says which side of
the line each claim stands on.

## What this guide covers

- [**What Kdenlive is**](what-kdenlive-is.md) —
  the mental model: instructions, not
  surgery, the engine underneath, and
  the permission rule
- [**The moving parts**](the-moving-parts.md) —
  bin, monitors, timeline, tracks,
  effects, scopes, and who holds what
- [**Installing Kdenlive**](installing-kdenlive.md) —
  the install, the version check, the
  companion renderer, and the folder
  shape to start with
- [**Your first project**](your-first-project.md) —
  profile, bin, rough cut, one title,
  and a render you actually watch
- [**Cutting and trimming**](cutting-and-trimming.md) —
  the razor, trims and ripples, gaps,
  and cutting sound apart from picture
- [**Audio and levels**](audio-and-levels.md) —
  decibels without tears, the level
  line, fades, normalising, and how
  loud a film should be
- [**Titles**](titles.md) —
  title clips, the title window, lower
  thirds, and what a title is in the
  file
- [**Transitions and effects**](transitions-and-effects.md) —
  dissolves, fades, the effect stack,
  and keyframes: the one idea under
  all three
- [**Colour and fixing shaky footage**](colour-and-fixing.md) —
  scopes, exposure, white balance, and
  what stabilising can and cannot
  recover
- [**Rendering and formats**](rendering-and-formats.md) —
  containers, codecs and bitrates,
  MP4 against WebM, and judging a
  render honestly
- [**Project files and keeping media together**](project-files-and-media.md) —
  the text file that is your film, the
  checkerboard that replaces missing
  media, and archiving
- [**Proxies for big footage**](proxies-for-big-footage.md) —
  small stand-ins for 4K monsters,
  measured: 86× smaller, 17× cheaper
  to decode
- [**Recipes**](recipes.md) — the
  middle ten seconds, a talk cleaned
  up, a slideshow, two cameras, one
  long recording made into episodes
- [**The neighbours**](the-neighbours.md) —
  Shotcut on the same engine, OpenShot
  the minimalist, and ffmpeg for
  surgery without re-encoding
- [**Limits**](limits.md) — unrecorded
  detail, variable frame rate, the
  speed budget, one editor at a time,
  and the preview that is only a
  promise
- [**Troubleshooting**](troubleshooting.md) —
  the INVALID title, the checkerboard,
  drifting sound, black previews, and
  the traps this guide's lab fell into
  so you don't have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Recording and capturing — cameras,
screen capture, live streaming — which
is a different craft with its own
tools (a related guide covers OBS
Studio). Cinema finishing: HDR grading
pipelines, surround mixing and
deliverables for broadcast are beyond
both this guide and, honestly, this
tool's centre of gravity. Dedicated
audio repair and music production
belong to audio tools. And other
people's footage as raw material:
chapter 1's rule is the whole position,
and no chapter quietly walks it back.

## How to use this guide

Read chapter 1 for the model and the
rule, and chapter 2 before installing
anything — knowing which part holds
what turns later confusion into a named
problem. Chapter 4 takes your first
project from empty folder to watched
render in one sitting; do that before
the technique chapters, which all
assume a rough film exists to improve.
Chapter 11 is the one to re-read when a
project breaks: most breakage is a
path, and the chapter shows you the
file so you can see it. The lab's
transcripts live in
`kdenlive-lab/transcripts/`; its project
and the script that wrote it are
`kdenlive-lab/project/` and
`kdenlive-lab/scripts/`; its media and
renders are beside them; its notes
are `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [OBS Studio for Mere Mortals](https://paulsullivan33-dev.github.io/obs-studio-for-mere-mortals/)
- [Audacity for Mere Mortals](https://paulsullivan33-dev.github.io/audacity-for-mere-mortals/)
- [ffmpeg for Mere Mortals](https://paulsullivan33-dev.github.io/ffmpeg-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/kdenlive-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/kdenlive-for-mere-mortals/blob/main/LICENSE-CODE).
