# The Neighbours

Kdenlive is one answer to "edit this
video". Three neighbours answer it
differently, and choosing honestly among
them starts with knowing they are not
the same shape of tool.

## Shotcut — the same engine, fewer rooms

**Shotcut** is built on the same MLT
engine as Kdenlive — the same melt
renderer this guide's lab drove, the
same project-file family. Its window is
deliberately simpler: fewer panels, a
gentler first hour, and a filter list
that reads like a menu rather than a
parts catalogue. What you give up is
depth: Kdenlive's effect stacks,
keyframing polish, scopes, proxy
handling and archiving are the fuller
toolkit. If editing is an occasional
afternoon, Shotcut's simplicity is a
real argument; if it is a habit, you
will move — and your MLT upbringing
moves with you, which is more than most
tool switches allow.

## OpenShot — the smallest complete answer

**OpenShot** aims at the smallest
possible complete editor: drag clips to
a timeline, trim, add a title from its
templates, export. Its animation
keyframing is friendly, its ambitions
are modest, and for a two-clip job it is
genuinely the fastest route from folder
to film. Its limits arrive with longer
timelines, heavy effects and fine audio
work — the ground chapters 5, 6 and 9
of this guide live on. OpenShot is the
right tool when the whole task is an
hour and the film is a kindness.

## ffmpeg — not an editor, and all the better for it

**ffmpeg** (a related guide covers it
fully) is the command-line media tool:
no window, no timeline, every operation
a command. For *surgery without
re-encoding* it beats every editor in
this chapter. Taking the middle of a
file, untouched, byte for byte:

```bash
ffmpeg -ss 00:04:00 -i long.mp4 -t 00:00:30 \
       -c copy excerpt.mp4
```

`-c copy` means the picture and sound
are copied, not recompressed: the job
takes seconds, the quality is the
original's, and the cut points snap to
the file's **keyframes** — the complete
pictures from which the codec rebuilds
the frames between — so the start may
land a fraction early. Editors re-encode
because they must be frame-exact and
because they mix and dress; when you
need none of that, ffmpeg is the honest
tool — joining files, converting
formats, extracting the sound, making
the proxy in chapter 12's table were all
one-liners of the same family. Half of
this guide's lab ran on it.

## Choosing

- One short job, lightest tool that
  finishes it: OpenShot or ffmpeg.
- Regular editing, room to grow, one
  tool to learn deeply: Kdenlive.
- Kdenlive's engine with a calmer
  window: Shotcut.
- Anything an editor cannot do at
  all — batch conversions, scripted
  cuts, a hundred files overnight:
  ffmpeg, possibly with melt behind it.

The professional suites (Premiere Pro,
DaVinci Resolve, Final Cut) are
neighbours of another kind: subscription
or studio-priced, with finishing depth
this guide's limits chapter waves at.
Nothing in this guide's films needed
them; knowing the border is part of
knowing the tool.
