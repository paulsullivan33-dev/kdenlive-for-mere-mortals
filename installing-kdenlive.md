# Installing Kdenlive

By the end of this chapter Kdenlive is on
your machine, you know its version, and
you know the one companion worth having
beside it. The lab installed it the
package-manager way on Linux; the other
routes are named honestly.

## The short version

- **Linux:** your distribution's package
  manager. On Ubuntu and Debian:
  `sudo apt install kdenlive`. A Flatpak
  from Flathub and an official AppImage
  also exist and are usually newer.
- **Windows and macOS:** the installer
  from kdenlive.org's download page.
- **Anywhere:** check what you got with
  the version line below.

The lab ran:

```bash
sudo apt install kdenlive melt
kdenlive --version
```

```text
kdenlive 23.08.5
```

The second package in that command,
**melt**, is MLT's command-line renderer
— Kdenlive's engine with a terminal
instead of a window. You do not need it
to edit. This guide's lab needed it
because the lab machine has no screen,
and everything the lab claims as *run*
was run through melt on real project
files (see `criteria.md`). If you install
it too, you own a useful diagnostic:
chapter 16 uses it to tell "the project
is fine" apart from "the window is
confused".

Version numbers matter more for editors
than for most tools: menus move between
releases, and a guide (this one included)
describes one generation — here, the
23.08 series. If your version differs,
expect the same ideas in slightly
different places, and trust the project's
own manual for your exact build.

Check: `melt -version` answers
`melt 7.22.0` on the lab machine, and
`ffmpeg -version` is worth running too —
Kdenlive leans on ffmpeg for much of its
reading and writing, and a broken ffmpeg
wears Kdenlive's clothes in bug reports.

## First run

Start Kdenlive once before you need it.
The first run creates its settings and a
default **project profile** — the shape
of film it assumes by default: picture
size, **frame rate** (frames per second),
and how the picture's proportions are
counted. The default (HD 1080p at 30
frames per second on many builds) is a
fine place to start; chapter 4 shows the
profile being chosen deliberately, and
chapter 11 explains why the profile
belongs to the project, not the clips.

Kdenlive also asks, on some builds,
whether to download extra resources and
whether it may use **GPU processing**
(Movit). Leave GPU processing off unless
you have a reason: it is the faster and
the fussier path, and chapter 16's black
preview lives there.

## Where things will live

Decide one folder for a project before
you start it — the project file and its
media in one tree, as chapter 11 insists.
The install creates nothing of yours;
your rendered films will land wherever
you point the rendering dialog, and your
project files wherever you save them. The
lab's arrangement is the model this guide
recommends:

```text
garden-tour/
  garden-tour.kdenlive     the project
  clips/                   the raw footage
  sound/                   music and narration
  renders/                 finished films
```

Check: you can state your Kdenlive and
MLT versions, and you have one empty
folder waiting with that shape. Chapter
4 puts a first film in it.
