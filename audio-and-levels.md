# Audio and Levels

By the end of this chapter your film
sounds deliberate: speech clear above
the music, nothing distorted, the whole
at a level a viewer does not have to
ride the volume control through. Sound
is half the film and the half beginners
neglect — viewers forgive a soft
picture; they abandon muddy sound.

## Levels, in one paragraph

Digital sound is measured in **decibels
below full scale** (dBFS). Zero is the
ceiling: a sample louder than 0 dBFS
cannot exist, and the attempt produces
**clipping** — the flat-topped, harsh
distortion you hear as crackle on loud
words. Everything you record lives below
zero; the craft is in *how far* below,
and in the *distance between* the parts.
Speech wants to sit clearly above music
and room sound, and peaks want to stay a
few dB under the ceiling: a working
target is speech peaks around −6 to
−3 dB, with music tucked well under
speech while anyone is talking.

Kdenlive shows you the evidence two ways:
the **waveform** drawn inside each audio
clip (its shape is the sound's shape —
tall is loud), and the meters in the
audio mixer and beside the monitor,
which report the level as it plays.

## The three controls

- **Clip volume.** Each audio clip has a
  volume, adjusted in its effect stack
  (the Volume effect) or by the level
  line on the clip itself. This is the
  per-clip fix: this interview is quiet,
  raise *it*.
- **Keyframes on the level line.** The
  line across an audio clip can be bent:
  double-click to add a point, drag
  points down under coughs, up under
  mumbles, and down-and-back-up where
  music should dip under speech — the
  dip is called **ducking** when music
  does it for a voice. A fade is the same
  idea at a clip's edge: the level walks
  from silence up, or down to silence.
- **Track faders in the mixer.** Each
  track's overall level, for balancing
  *families* of sound (all the music
  against all the voice) once the clips
  are individually sane.

## What a fade is, in the file

The lab verified the fade the way the
guide verifies everything: in the file,
and in the render. An audio fade is a
**volume filter** on the track whose
level is keyframed in decibels —

```xml
<filter id="fade_in" in="00:00:00.000" out="00:00:00.999">
 <property name="level">0=-60; 24=0</property>
 <property name="mlt_service">volume</property>
</filter>
```

— and the rendered film's measured level
obeys it: −69.4 dB (silence, for practical
purposes) across the first fraction of a
second, rising to the tone's full
−24.1 dB once the fade completes
(`kdenlive-lab/transcripts/t03`). When
you drag a fade corner in the window, this
filter is what you are writing.

## Normalising and the loudness target

If a whole recording is simply too quiet,
the **normalise** analysis (a clip job /
audio effect in Kdenlive) measures it and
raises it so its loudest peak reaches a
level you choose. Normalising fixes
*overall* level only; it cannot fix a
recording whose quiet parts are too quiet
*relative* to its loud parts — that is
compression, an audio effect Kdenlive
carries, and a bigger topic than one
paragraph; the honest beginner's move is
to re-record or to ride the level line by
hand.

For films headed to the big video sites,
the loudness rule of thumb is an overall
loudness near **−14 LUFS** (LUFS is
loudness measured the way ears hear it,
averaged) with peaks at or below −1 dB.
Kdenlive's loudness analysis tools can
report a mix's LUFS; treat the number as
a sanity check, not a target to chase
into distortion.

## Sound at the cut

Two small habits from chapter 5's world:
a cut in sound is more noticeable than a
cut in picture, so let room sound run
under picture cuts where you can; and a
two-frame audio **crossfade** — one clip
fading out as the next fades in — hides
the click that a hard sound cut often
makes. Both are level-line work, nothing
more.

Check: in your film, pull the music down
6 dB under the speech with two keyframe
points, add a one-second fade-in at the
very start, render ten seconds, and
listen on headphones: music present but
behind, opening smooth, meters never
touching zero.
