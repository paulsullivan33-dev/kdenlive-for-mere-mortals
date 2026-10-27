# Proxies for Big Footage

By the end of this chapter you will know
how to keep editing smoothly when the
footage is bigger than your computer's
patience: **proxy clips** — small
stand-ins that the editor works with
day to day, swapped back for the
originals at render time.

## The problem, measured

Modern cameras record 4K and beyond, in
codecs chosen for small files, not for
being decoded sixty times a second while
you scrub. Editing is decode-hungry work:
every jog of the playhead, every preview,
is the footage being read again. When
the machine cannot keep up, the preview
stutters, the playhead lags behind your
hand, and editing turns to porridge.

The lab measured the gap on a two-second
3840×2160 clip it made for the purpose,
and its 640×360 stand-in:

| | Original 4K | Proxy 640×360 |
|---|---|---|
| Size on disk | 4,329,480 B | 50,375 B |
| Time to decode every frame | 1.49 s | 0.09 s |

The proxy is **86× smaller** on disk and
about **17× cheaper to decode**
(`kdenlive-lab/transcripts/t06`). An
editor does not care about the clip's
file size for its own sake; it cares
about that second row, constantly.

## How Kdenlive's proxies work

Kdenlive will make proxies for you:
Settings → Configure Kdenlive → Proxy
Clips turns the feature on and sets the
recipe (how wide, which codec); after
that, adding a big clip offers — or, per
settings, begins — a background **proxy
job** that writes a small copy of the
clip into the project's proxy folder.
A clip wearing a proxy shows a small
badge in the bin. From then on:

- The timeline, the monitors and every
  cut work on the **proxy**. Editing is
  light and quick; the picture you judge
  by is softer, which matters for cuts
  and levels and not at all for story.
- The **render** quietly uses the
  **originals**. Nothing about the
  output changes — same profile, same
  quality. The swap is the entire point,
  and it is automatic.
- Individual clips can be proxied or
  un-proxied from the bin's right-click
  menu, so a small project can proxy
  only its two monsters.

Proxy settings worth a decision: width
(half or quarter of the original is
typical; the lab used 640 wide), and
storing proxies inside the project
folder, where chapter 11's archiving
habit keeps them with everything else.
Proxies are derived files — delete them
and nothing is lost but the time to
remake them — so they need no backup
beyond the project.

## When proxies are the wrong medicine

- **Small footage.** 1080p from a modest
  camera on a healthy machine edits
  fine; proxying it adds jobs and
  clutter for nothing.
- **Colour judgements.** Chapter 9's
  scopes read the proxy while you edit,
  and a heavily compressed proxy *lies*
  a little about fine colour and noise.
  Do final colour with proxies off
  (Kdenlive can disable them for the
  session) on the hero shots.
- **The render was never the problem.**
  Proxies speed editing, not rendering:
  the render reads the originals and
  takes what it takes (chapter 10).

A cousin worth naming: **transcoding**.
Where proxies are temporary stand-ins,
a transcode replaces a hostile original
(notoriously, phone footage with a
*variable frame rate*, chapter 15) with
a friendly editing copy for good.
Kdenlive offers transcode jobs in the
same bin menus. Proxies first; transcode
when the footage itself misbehaves.

Check: take the biggest clip you own,
note how the preview behaves while you
scrub it, make its proxy, and scrub
again. The difference you feel is the
second row of the table above, in your
hand.
