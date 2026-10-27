# Cutting and Trimming

By the end of this chapter you can take a
rough assembly apart and put it back
tighter: cut a clip where the moment
changes, trim heads and tails to the
exact frame, close the gaps, and undo
your way out of any of it. This is the
chapter where editing happens; the rest
is dressing.

## The razor: cutting one clip into two

The **razor tool** (on the timeline
toolbar) cuts the clip under the
playhead into two clips. Nothing is lost
— both halves still point into the same
source file, and each can be re-extended
later — but each half can now be moved,
deleted, or dressed independently. Cut
where the shot changes its mind: the
camera settles, the speaker starts the
real sentence, the dog finally jumps.

The editing pattern the razor enables is
the most common one in all of film:

1. Play the clip in the timeline; pause
   where the good part starts.
2. Cut there. Cut again where it ends.
3. Delete the outside pieces (select,
   Delete), and close up (below).

## Trimming: the ends are handles

A clip's ends are handles. Drag the left
end right and the clip starts later in
its source; drag it back left and the
material returns. Trimming changes what
the timeline *shows*, never the source
file — the frames are still in the clip,
only out of view, which is why a trim is
always safe to undo by dragging back.

Two trims have names worth knowing.
**Ripple** trimming moves everything
after the trim point with it, so the
timeline stays closed — no gap appears.
Plain trimming leaves a gap, which the
**spacer tool** closes by dragging a
whole group of clips left. Beginners
lose more time to unexplained gaps than
to everything else in this chapter
combined; when the film has a black hole
in the middle, a gap is what it is.

Kdenlive shows the neighbouring frames as
you drag an edge, and snapping (to the
playhead, to other clips' edges) can be
toggled — snap on while arranging, off
for frame-fine work.

## Cutting sound and picture apart

Video clips with sound arrive linked:
cut one and you cut both. Sometimes that
is the point — keep a speaker's voice
running over the next shot and the film
suddenly feels professional. **Ungroup**
(the clip's right-click menu) separates
the sound from the picture so each can be
cut and trimmed alone. The two classic
shapes have names: a **J-cut** starts the
next shot's sound before its picture; an
**L-cut** lets the previous sound linger
under the next picture. Both are just
ungrouped clips trimmed with intent.

## What the file says a cut is

A cut is not surgery on media; it is two
numbers. Every timeline clip carries an
**in point** and an **out point** into
its source — "from 00:04 to 00:09" — and
the razor writes a second clip whose
numbers continue where the first stopped.
The lab's project file shows it plainly,
two entries end to end on one track:

```xml
<entry producer="clip_gate"  in="00:00:00.000" out="00:00:02.999"/>
<entry producer="clip_roses" in="00:00:00.000" out="00:00:02.999"/>
```

That is why nothing in this chapter can
damage your footage, and why a project
file is kilobytes while its media is
gigabytes (chapter 11).

## Working habits that survive contact

- Cut on movement or on the breath
  before speech; a cut mid-gesture hides
  itself.
- Watch the project monitor, not the
  timeline, when judging a cut. The
  timeline shows structure; only the
  monitor shows the film.
- Keep one untouched track or one saved
  copy of the project (`Save As` with a
  version in the name) before a big
  restructure. Undo is deep, but a saved
  copy is deeper.

Check: take your chapter-4 film, cut ten
seconds of dead air out of the middle
with the razor, ripple the gap closed,
and play it — the film is shorter, the
join is invisible in the monitor, and
dragging the second half's left edge
restores the cut seconds, proving the
trim destroyed nothing.
