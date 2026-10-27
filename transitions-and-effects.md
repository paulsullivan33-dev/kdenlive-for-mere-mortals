# Transitions and Effects

By the end of this chapter you can soften
a cut into a dissolve, fade a film in and
out, and dress a clip with an effect
whose strength changes over time — and
you will know the one idea underneath all
three, because they are all the same
idea.

## Transitions: how one shot becomes another

A **transition** governs the moment two
clips meet. The plain meeting — one ends,
the next begins — is the **cut**, and it
is the right choice far more often than
beginners believe. The others earn their
place sparingly:

- **Dissolve (crossfade).** The first
  shot fades out as the second fades in.
  In Kdenlive, drag one clip so it
  overlaps the other on the timeline (or
  use the transition handle at a clip's
  corner) and the overlap becomes a
  dissolve. Use it for time passing, or
  between scenes — not between every
  shot, where it turns to soup.
- **Fade from/to black.** A dissolve
  against nothing: the picture sinks to
  black, or rises from it. It opens and
  closes films, and separates chapters
  inside them. In the file it is not a
  transition at all but chapter 2's
  brightness effect keyframed down — the
  lab's project fades its first second up
  from black exactly that way, and the
  rendered frames measure it: mean luma
  19.7 at frame 2, 45.8 at frame 12,
  90.7 once the fade completes
  (`kdenlive-lab/transcripts/t03`).
- **Wipes.** One shot pushes the other
  off the screen in a pattern. Kdenlive
  ships a shelf of them (the luma
  transitions, with pattern images). They
  date a film faster than any other
  choice in this chapter; know they
  exist, and reach rarely.

Underneath, a transition in the file is a
note in the timeline saying *blend these
two tracks across these frames* — the
engine (MLT) does the blending, with
services named in the lab's project
file: `mix` for sound, a
compositing transition for picture.

## Effects: instructions pinned to a clip

An **effect** changes a clip while it
plays: brightness, contrast, blur,
sharpen, volume, pan, transform (move,
resize, rotate the picture inside the
frame). Add one by selecting the clip and
choosing from the Effects panel; it lands
in the clip's **effect stack** (chapter
2), where its sliders live and where it
can be ticked off to compare before and
after — the honest way to judge any
effect.

Three habits keep effects safe:

1. **One at a time, then compare.**
   Effects stack in order; an effect you
   cannot hear or see the absence of is
   ballast.
2. **Transform is the mover.** Reframing
   a shot — a gentle zoom into a still
   photo, pushing in on a speaker — is
   the Transform effect with keyframes,
   below.
3. **Audio effects are chapter 6's
   tools** wearing effect clothing:
   volume, pan (left-right balance), and
   the repair shelf. Same stack, same
   rules.

## Keyframes: values that walk

Most effect values can be **keyframed**:
pin the value at one frame, pin a
different value later, and the engine
walks smoothly between them. The walk is
what a fade is (volume or brightness,
pinned low then high), what a slow zoom
is (transform scale, pinned at 100% then
110%), what a title's drift is. The
keyframe editor sits under an effect's
sliders; double-click adds a pin, drag
moves one. Curves between pins can be
linear (steady walk) or smooth (slow
starts and landings) — smooth is the
default your eyes prefer for fades, and
the choice is a property of each pin.

The file shows a keyframe set the way
this whole guide shows things — as text
small enough to check:

```xml
<property name="level">0=0; 24=1</property>
```

reads "at frame 0 the value is 0; at
frame 24 it is 1". Everything in this
chapter, however it was made in the
window, lands in the project as lines
like that (chapter 11).

Check: dissolve between your film's
first two clips by overlapping them half
a second; fade the whole film in from
black over one second and out at the
end; then untick each in the stack and
play again. If you can say what each one
added — and the film is better *with*
restraint than without — the chapter has
done its work.
