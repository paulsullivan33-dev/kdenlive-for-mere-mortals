# Troubleshooting

The failures this guide's lab met, and
the ones the documentation and long
experience say you will. Each entry is
the symptom, the cause, and the way
out — in that order, because the symptom
is what you have.

## The title renders as the word INVALID

**Symptom:** a rendered file shows
INVALID in giant letters where a title
should be; the same project previews
fine in the window.

**Cause:** the title is drawn by MLT's
Qt module, which needs a display. A
render driven from a script, a scheduler
or a headless machine has none, and the
engine substitutes a placeholder. The
lab reproduced this exactly: melt's own
error names it — "The MLT Qt module
requires a X11 environment"
(`kdenlive-lab/transcripts/t03`).

**Way out:** render where a display
exists (the desktop app), or give the
renderer a fake one — `xvfb-run -a melt
…` on Linux. On a normal desktop this
failure does not occur; in a script it
is the first thing to check.

## A clip's slot in the film is a grey checkerboard

**Symptom:** part of the render is a
grey checkerboard pattern; the render
finished without complaint.

**Cause:** the media file is not where
the project says it is — moved, renamed,
on an unmounted drive — and the engine
drew its placeholder instead (verified
in `kdenlive-lab/transcripts/t05`).

**Way out:** put the file back, or open
the project and let Kdenlive's missing
clip search find it in its new home;
then adopt chapter 11's one-folder
habit so it stops happening.

## The clip is flagged missing when the project opens

The same cause, caught earlier and more
politely. Do not delete the clip from
the bin and re-add it (that loses its
edits); mend the path. If the file is
truly gone, the timeline still holds
its slot and timing — a re-shot or a
stand-in drops into the same hole.

## The preview is black, frozen, or shows the wrong frames

**Cause, in the order to check them:**
GPU processing (Movit) disagreeing with
your drivers — turn it off in Settings
and try again; a proxy still being
generated (wait for the job, watch the
bin badge); or a clip the engine cannot
decode at all (an exotic codec —
transcode it, chapter 15).

**A separating test:** render five
seconds around the bad moment with
melt, the command-line renderer
(chapter 10 shows the shape). If melt's
frames are right, the project and media
are fine and the problem is the
window's display path; if melt agrees
with the window, the problem is in the
project or the footage, and you have
halved the search either way.

## Sound drifts away from the picture

Grows worse the longer the clip runs:
the signature of **variable frame rate**
footage (chapter 15). Transcode the
clip to a constant frame rate and
replace it in the project. Sync that is
wrong by the same amount everywhere is
a different, happier fault: the clip
was placed or trimmed a few frames off,
and nudging cures it.

## Clicks and pops at the cuts

Hard cuts in sound click. Put a
two-frame audio crossfade (chapter 6)
across the join, or bend the level line
to zero exactly at the cut and back up
after it. If every cut clicks, suspect
the source recording, not the edit.

## The render takes forever

Forever has a budget you can read:
count the effects (chapter 8) on the
busiest stretch and the picture size in
the profile. Pre-render the heaviest
clip to a new file (render just its
range, replace the clip with the
result), drop two-pass for tests, and
let final renders run overnight without
guilt — a render is the one part of
editing that improves by being left
alone.

## The film looks different after uploading

Usually the site's re-encode, not your
render: compare the uploaded copy
against your file played locally, not
against the Kdenlive monitor. If the
local file itself looks washed out where
the monitor looked rich, suspect a
levels-range mismatch (some players
read video levels differently); the
fix is a render setting, and the test
is chapter 10's: judge files, not
previews.
