# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's film is six seconds of generated colour and tone.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 15 names what the tool
   cannot do: detail that was clipped, blurred or never
   recorded cannot be recovered; variable frame rate footage
   fights the timeline until it is transcoded; effects spend
   the machine's speed and proxies relieve editing, not
   rendering; there is one editor per project and no live
   collaboration; and sound repair stops at the studio door.
8. **The permission rule is in the text, early.** Chapter 1
   and the README state it plainly — *your footage, or footage
   you have clear permission to use, music included* — before
   any procedure depends on it, and later chapters point back
   to it where the tooling makes crossing the line easy, such
   as a slideshow's soundtrack.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox
with **no display**. Kdenlive **23.08.5** and melt **7.22.0**
were installed with apt, alongside the ffmpeg/ffprobe 8.1.2
the machine already carried. Everything the lab verified,
it verified through the project file and the MLT renderer
(melt, the engine Kdenlive renders through) — the layers
that leave evidence — and never through the editing window,
which this machine cannot show. All transcripts live in
`kdenlive-lab/transcripts/`; the lab project is
`kdenlive-lab/project/garden-tour.kdenlive`, written by
`kdenlive-lab/scripts/make_lab_project.py`.

Run for real, with transcripts as evidence:

- Install and version of Kdenlive, melt and ffmpeg (t00).
- The fixture media generated with ffmpeg and read back with
  ffprobe: two 3-second 1280×720 25 fps clips, a 6-second
  tone, a 2-second 3840×2160 test clip (t01).
- A minimal project in Kdenlive's own file format — main
  bin, three timeline tracks, a title clip whose layout
  follows a template Kdenlive ships, a brightness fade from
  black and a volume fade-in — rendered with melt to MP4
  and read back with ffprobe: H.264 1280×720 video, AAC
  stereo audio, 150 frames, 6.016 s (t02).
- The title and both fades verified on the rendered file,
  not the project: extracted stills show the title over
  the first clip (checked by eye); mean frame luma climbs
  19.7 → 45.8 → 90.7 across the fade from black; audio RMS
  climbs from −69.4 dB in the fade's first fraction to
  −24.1 dB at full level (t03).
- The same project rendered to WebM and read back:
  VP9 video, Opus audio, 6.008 s (t04).
- Missing-media behaviour: a copy of the project with one
  path broken renders to completion, and the missing
  clip's slot is a grey checkerboard (t05).
- Proxy arithmetic on the 4K clip: a 640×360 proxy is
  50,375 bytes against the original's 4,329,480 (86×
  smaller) and decodes in 0.09 s against 1.49 s (about
  17× cheaper), measured with ffmpeg (t06).
- The lab's own trap, also run for real: rendered without
  a display, the title came out as the word INVALID,
  because MLT's Qt module needs an X11 environment;
  rendering under xvfb-run (a fake X server) fixed it,
  and the diagnosis is chapter 16's first entry (t03).

Documented only — described from Kdenlive 23.08's
documentation, not run, and the text does not claim
otherwise:

- Everything done with the mouse in the editing window:
  dragging clips to the timeline, razor and trim gestures,
  snapping, the Insert/Overwrite tools, group and ungroup.
- The title window's design work (the lab's title was
  authored as a file in Kdenlive's title format and its
  *rendering* is verified; the window itself was never
  opened).
- Keyframing by hand in the effect stack and keyframe
  editor (the lab's fades were authored as keyframe lines
  in the project file, and their effect on the render is
  measured; the dragging is documented).
- The audio mixer's faders, the loudness analysis tools,
  and the normalise clip job.
- Colour correction in the window and the scopes' use
  (chapter 9); the Stabilize clip job and its vid.stab
  analysis pass; proxy *clip jobs* inside Kdenlive (the
  proxy in t06 was made and measured with ffmpeg — the
  sizes and decode costs are the verified part, the menu
  steps are documented).
- The rendering dialog's presets and two-pass option
  (the lab rendered with melt, the dialog's engine,
  spelling the same choices as command-line properties).
- The Archive Project tool's behaviour (chapter 11 states
  what it does; the lab's one-folder discipline was
  verified by moving directories, not by running the
  archiver).
- The comparison tools in chapter 14 are characterised,
  not benchmarked.

Fixtures are this guide's own and deliberately generic: a
six-second "garden tour" assembled from two generated
colour clips with burnt-in labels, a generated tone, and
a title in Kdenlive's title format. No example is
modelled on any real person, organisation, event or
recording, and no real footage appears anywhere in the
guide.
