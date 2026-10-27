# Your First Project

By the end of this chapter you have a
short film that plays: three clips in a
row, a title over the first, sound
underneath, and a rendered file you can
hand to anyone. It will not be pretty.
It will be *finished*, which is the skill
every later chapter refines.

The lab's version of this project —
invented footage of a fictional garden
tour — is kept in the repository
(`kdenlive-lab/`), where the render was
verified frame by frame. Your version
uses your own clips; the steps are the
same. Steps done with the mouse in the
editing window are described from
Kdenlive's documented behaviour;
`criteria.md` keeps the exact ledger of
what the lab ran and what it only read.

## 1. Make the project, choose the profile

File → New. Before anything else, set the
**project profile** (Project → Project
Settings): picture size and frame rate
matching your footage — 1920×1080 at your
camera's frame rate for most phone and
camera clips. The profile is the film's
canvas. Clips of other sizes are fitted
to it; a profile chosen wrong is a film
that letterboxes or stutters, and it is
much easier to choose now than to change
later.

Save immediately (File → Save As) into
your project folder, with a real name:
`garden-tour.kdenlive`. From here on,
save often — the project file is small,
and it is the only copy of your
arrangement.

## 2. Fill the bin

Project Bin → Add Clip (or drag files
in). Add two or three short clips and one
sound file. Each appears with its length;
the files themselves stay where they are
— the bin now holds their paths (chapter
2's warning, arriving on schedule).

Audition in the **clip monitor**: click a
clip, press play, and mark the stretch
worth using with I (in) and O (out). Ten
honest seconds chosen here save a minute
of trimming later.

## 3. Build the timeline

Drag the marked stretch to a video track
(the **Insert** or **Overwrite** tool, or
simply drop it at the playhead). Add the
second clip after it, the third after
that. Drag the sound file to an audio
track, starting at the same moment as the
first picture.

Play it in the project monitor. What you
have is a rough assembly — editors call
this stage the **rough cut**, and every
real film passes through it. Chapter 5
turns rough into deliberate.

## 4. One title

Create a title clip (Project Bin → Add
Title Clip), type the film's name, and
place it on the video track *above* the
first clip, for its first two seconds.
That is chapter 7 in embryo: words live
on a higher track, over the picture, for
exactly as long as they are on the
timeline.

## 5. Render, then watch the render

Press Render, accept the MP4 preset,
name the output into your `renders/`
folder, and wait. Then — the step
beginners skip — play the rendered file
in an ordinary player, all the way
through. The render is the film; the
timeline is only its recipe.

That discipline is the lab's own: it
rendered its six-second project twice
(MP4 and WebM) and verified the files
with ffprobe — a tool that reports a
video file's contents — rather than
trusting that the render "looked right":

```text
video: h264, 1280x720, 25 fps
audio: aac, 48000 Hz, stereo
duration: 6.016s   (150 frames; the extra
                   0.016s is container padding)
```

Check: your rendered file plays from
start to finish in a normal player, with
picture, title and sound in the right
order. Everything after this chapter is
about making that film *better*, one
named skill at a time.
