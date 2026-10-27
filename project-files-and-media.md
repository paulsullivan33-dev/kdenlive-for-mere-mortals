# Project Files and Keeping Media Together

By the end of this chapter your projects
will still work next year: you will know
what a `.kdenlive` file actually holds,
why it is tiny while its films are huge,
and the one folder habit that prevents
the commonest disaster in all of editing.

## The project file is a text file

A `.kdenlive` project is XML — structured
text, readable in any text editor — in
the MLT engine's format. Here is the
heart of the lab's project, the bin and
one clip, almost complete:

```xml
<playlist id="main_bin">
 <entry producer="clip_gate" in="00:00:00.000" out="00:00:02.999"/>
 ...
</playlist>
<producer id="clip_gate" ...>
 <property name="resource">../media/clip-a-gate.mp4</property>
 <property name="mlt_service">avformat-novalidate</property>
 <property name="kdenlive:clipname">clip-a-gate</property>
</producer>
```

Read it as it asks to be read. The bin
(`main_bin`) lists the clips. Each clip
names a **resource** — a path to a media
file — and the engine service that reads
it. The timeline is more lists like
this: tracks holding clips with in and
out points (chapter 5), filters holding
effects (chapter 8). The whole of your
editing — every cut, fade and title —
is lines like these. That is why the
file is kilobytes.

**The media is not in the project.** Not
a frame of it, not a sample of the
sound. The project holds *paths and
instructions*; the media stays in its
own files, read fresh every time the
project opens or renders.

## What happens when a path breaks

The lab broke one on purpose. It copied
its project, pointed one clip at a file
that does not exist, and rendered. The
render did not refuse and did not stop:
it completed, and the missing clip's
three seconds came out as a grey
**checkerboard** — the engine's
placeholder for a picture it cannot read
(`kdenlive-lab/transcripts/t05`).

That silence is the dangerous part. In
the editing window a missing clip is
flagged when the project opens, and
Kdenlive offers to search a folder for
the file and mend the path. A headless
render — or one you do not check —
says nothing: the film ships with
checkerboard in it. Hence the two rules
of this chapter:

1. **Keep a project and its media in
   one folder tree**, and move the tree,
   never the pieces. Relative paths
   (like the lab's `../media/...`) keep
   working wherever the tree goes;
   absolute paths break the moment the
   tree moves house.
2. **Check every render** (chapter 10's
   habit), because the render is where a
   broken path confesses.

## The archiving habit

For a finished project you mean to keep,
Kdenlive has the right tool built in:
**Project → Archive Project** copies the
project file and every media file it
points at into one folder, rewriting the
paths to match. Archive once, and the
project is immune to the tidying that
scatters media over the following years:
the downloads folder purge, the "old
videos" drive, the renamed directory.

Daily discipline is smaller: one folder
per project with the shape from chapter
3 (project at the top, `clips/`,
`sound/`, `renders/` beneath), imports
copied *into* the folder rather than
referenced from wherever the camera card
happened to mount, and the project
saved with a name that says what it is.
Back that folder up the way you back up
anything irreplaceable — which, once
edited, it is: the media can be
re-downloaded from a camera about never.

Check: open your `.kdenlive` in a text
editor and find one clip's `resource`
line. Rename the media *folder* (not the
file), open the project, watch Kdenlive
report the clip missing — then rename
the folder back and see it heal. You
have now met the disaster in its
harmless form, which is the only safe
way to meet it.
