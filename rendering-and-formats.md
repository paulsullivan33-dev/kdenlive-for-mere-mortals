# Rendering and Formats

By the end of this chapter you can turn
a project into the right finished file
for its destination, and you can predict
the trade you are making: every render
is a bargain between file size, picture
quality, and how widely the result will
play.

## Rendering, in one paragraph

**Rendering** (also called exporting) is
the engine reading your project —
every clip at its in and out points,
every effect, every mix — and writing
one new video file, frame by frame.
Nothing is written back to the project or
the media. A render is always safe to
re-do with different choices, which is
why this chapter's advice is to render
small tests rather than agonise.

In the window: the Render button opens
the rendering dialog; you pick a
destination file, a **preset**, and
Render to File. The lab, having no
window, drove the same engine (MLT) from
the command line — and the command is
worth seeing once, because it is exactly
the dialog with the words spelled out:

```bash
melt garden-tour.kdenlive -consumer avformat:garden-tour.mp4 \
     vcodec=libx264 pix_fmt=yuv420p acodec=aac ab=128k
```

*Read the project; write an MP4; video
encoded as H.264; audio as AAC at
128 kbit/s.* Every preset in the dialog
is a bundle of choices like these.

## The three words that decide everything

Confusion in this area is always a mix-up
among three different things:

- The **container** is the wrapper and
  the file's surname: MP4, WebM, MOV,
  MKV. It decides almost nothing about
  quality.
- A **codec** is the method the picture
  or sound was compressed with: H.264,
  VP9, H.265 for picture; AAC, Opus for
  sound. Codecs decide quality per byte
  and who can play the file.
- The **bitrate** is how many bits per
  second the codec may spend: more bits,
  better picture, bigger file. This, not
  the container, is your quality dial.

## The two renders the lab made

The lab rendered one six-second project
both honest ways, and the files are in
the repository to inspect:

| File | Container | Video | Audio | Size | Length |
|---|---|---|---|---|---|
| garden-tour.mp4 | MP4 | H.264 | AAC | 180,207 B | 6.016 s |
| garden-tour.webm | WebM | VP9 | Opus | 170,578 B | 6.008 s |

Same timeline, same six seconds. For
*this* simple synthetic film the sizes
land close; real footage spreads them
further apart, and VP9 usually wins on
size at equal quality while H.264 wins
on compatibility and render speed. Which
brings up the choosing:

- **MP4 with H.264 + AAC** is the
  universal default: phones, televisions,
  browsers, group chats, the lot. When
  in doubt, this is the render.
- **WebM with VP9 + Opus** is the web's
  own format: open, efficient, ideal for
  embedding in pages; some desktop
  players and older devices still trip
  on it.
- **MOV / MKV** appear as camera
  originals and editing intermediates
  more than as delivery formats for
  mere mortals.

## Settings that matter, settings that don't

Picture **size** and **frame rate**
come from the project profile (chapter
4) — a render cannot add detail the
profile threw away, so a "4K render" of
a 720p project is a 720p film in a heavy
coat. **Quality** in the dialog (a
bitrate or a quality slider depending on
preset) is the real dial: for 1080p
H.264, somewhere around 8–16 Mbit/s is
honest quality; the big upload sites
will re-encode whatever you send, so
sending more than that mostly buys
upload time. Two-pass rendering (an
option in the dialog) spends a first
pass studying the film to spend the
second pass's bits wisely — worth it
for a final render of anything long,
pointless for tests.

What does not matter nearly as much as
forums suggest: the container (pick for
the audience), and small differences in
audio bitrate for speech (128 kbit/s AAC
is already transparent for voices).

## Render in pieces, check in players

For a long film, render a thirty-second
test from the busiest section first —
the section with the most movement is
where a too-low bitrate shows as mush —
and judge *that*, in a player, at full
screen, before committing an hour to the
whole. And always check the finished
render the chapter-4 way: play it
somewhere that is not Kdenlive. The lab's
habit travels well: it read its renders
back with ffprobe (streams, size,
duration) *and* extracted stills to look
at — a render that reports correctly
and looks right is a render you can
ship.

Check: render your film as MP4 and as
WebM, compare the two sizes and the two
plays, and write down which you would
send to (a) a family group chat and
(b) your own web page. If the answers
differ and you can say why, this chapter
has done its work.
