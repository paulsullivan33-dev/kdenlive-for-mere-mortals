#!/usr/bin/env python3
"""Author the lab's minimal Kdenlive project: garden-tour.kdenlive.

The project is written in Kdenlive's own file format (MLT XML):
a main_bin playlist holding the clips, one playlist per timeline
track, and a timeline tractor that composites them. Media paths
are relative to the project file, so the checkout can move.

Timeline (25 fps, 150 frames = 6 seconds):
  V2  title clip, frames 0-49 ("A Short Garden Tour")
  V1  clip-a-gate 0-74, clip-b-roses 75-149, fade from black 0-24
  A1  tone.wav 0-149, fading in over frames 0-24
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent / "project" / "garden-tour.kdenlive"
TITLE = HERE.parent / "project" / "garden-title.kdenlivetitle"

TITLE_XML = """<kdenlivetitle width="1280" height="720" out="49">
 <item z-index="0" type="QGraphicsTextItem">
  <position x="215" y="308">
   <transform>1,0,0,0,1,0,0,0,1</transform>
  </position>
  <content font-color="255,255,255,255" font-outline-color="0,0,0,255" font-pixel-size="76" font-italic="0" font-underline="0" font-weight="50" font="DejaVu Sans" font-outline="2">A Short Garden Tour</content>
 </item>
 <startviewport rect="0,0,1280,720"/>
 <endviewport rect="0,0,1280,720"/>
 <background color="0,0,0,0"/>
</kdenlivetitle>
"""

PROJECT_XML = """<?xml version="1.0" encoding="utf-8"?>
<mlt LC_NUMERIC="C" version="7.22.0" title="A Short Garden Tour" producer="timeline">
 <profile description="Custom" width="1280" height="720" display_aspect_num="16" display_aspect_den="9" sample_aspect_num="1" sample_aspect_den="1" colorspace="709" frame_rate_num="25" frame_rate_den="1" field_order="1" seekable="1"/>
 <playlist id="main_bin">
  <property name="xml_retain">1</property>
  <entry producer="clip_gate" in="00:00:00.000" out="00:00:02.999"/>
  <entry producer="clip_roses" in="00:00:00.000" out="00:00:02.999"/>
  <entry producer="clip_tone" in="00:00:00.000" out="00:00:05.999"/>
  <entry producer="clip_title" in="00:00:00.000" out="00:00:01.999"/>
 </playlist>
 <producer id="clip_gate" in="00:00:00.000" out="00:00:02.999">
  <property name="length">00:00:03.000</property>
  <property name="eof">pause</property>
  <property name="resource">../media/clip-a-gate.mp4</property>
  <property name="ttl">1</property>
  <property name="aspect_num">1</property>
  <property name="aspect_den">1</property>
  <property name="mlt_service">avformat-novalidate</property>
  <property name="seekable">1</property>
  <property name="kdenlive:clipname">clip-a-gate</property>
 </producer>
 <producer id="clip_roses" in="00:00:00.000" out="00:00:02.999">
  <property name="length">00:00:03.000</property>
  <property name="eof">pause</property>
  <property name="resource">../media/clip-b-roses.mp4</property>
  <property name="ttl">1</property>
  <property name="aspect_num">1</property>
  <property name="aspect_den">1</property>
  <property name="mlt_service">avformat-novalidate</property>
  <property name="seekable">1</property>
  <property name="kdenlive:clipname">clip-b-roses</property>
 </producer>
 <producer id="clip_tone" in="00:00:00.000" out="00:00:05.999">
  <property name="length">00:00:06.000</property>
  <property name="eof">pause</property>
  <property name="resource">../media/tone.wav</property>
  <property name="ttl">1</property>
  <property name="mlt_service">avformat-novalidate</property>
  <property name="seekable">1</property>
  <property name="kdenlive:clipname">tone</property>
 </producer>
 <producer id="clip_title" in="00:00:00.000" out="00:00:01.999">
  <property name="length">00:00:02.000</property>
  <property name="eof">pause</property>
  <property name="resource">garden-title.kdenlivetitle</property>
  <property name="ttl">1</property>
  <property name="aspect_num">1</property>
  <property name="aspect_den">1</property>
  <property name="mlt_service">kdenlivetitle</property>
  <property name="seekable">1</property>
  <property name="kdenlive:clipname">Garden title</property>
 </producer>
 <playlist id="track_video">
  <entry producer="clip_gate" in="00:00:00.000" out="00:00:02.999"/>
  <entry producer="clip_roses" in="00:00:00.000" out="00:00:02.999"/>
  <filter id="fade_from_black" in="00:00:00.000" out="00:00:00.999">
   <property name="window">75</property>
   <property name="max_gain">20dB</property>
   <property name="level">0=0; 24=1</property>
   <property name="mlt_service">brightness</property>
  </filter>
 </playlist>
 <playlist id="track_audio">
  <entry producer="clip_tone" in="00:00:00.000" out="00:00:05.999"/>
  <filter id="fade_in" in="00:00:00.000" out="00:00:00.999">
   <property name="window">75</property>
   <property name="max_gain">20dB</property>
   <property name="level">0=-60; 24=0</property>
   <property name="mlt_service">volume</property>
  </filter>
 </playlist>
 <playlist id="track_title">
  <entry producer="clip_title" in="00:00:00.000" out="00:00:01.999"/>
  <blank length="00:00:04.000"/>
 </playlist>
 <tractor id="timeline" in="00:00:00.000" out="00:00:05.999">
  <property name="kdenlive:docproperties.profile">custom</property>
  <property name="kdenlive:docproperties.framerate">25/1</property>
  <track producer="track_video"/>
  <track producer="track_audio"/>
  <track producer="track_title"/>
  <transition id="mix_audio_1">
   <property name="a_track">0</property>
   <property name="b_track">1</property>
   <property name="mlt_service">mix</property>
   <property name="always_active">1</property>
   <property name="sum">1</property>
  </transition>
  <transition id="blend_title_1">
   <property name="a_track">0</property>
   <property name="b_track">1</property>
   <property name="mlt_service">frei0r.cairoblend</property>
   <property name="always_active">1</property>
  </transition>
  <transition id="mix_audio_2">
   <property name="a_track">0</property>
   <property name="b_track">2</property>
   <property name="mlt_service">mix</property>
   <property name="always_active">1</property>
   <property name="sum">1</property>
  </transition>
  <transition id="blend_title_2">
   <property name="a_track">0</property>
   <property name="b_track">2</property>
   <property name="mlt_service">frei0r.cairoblend</property>
   <property name="always_active">1</property>
  </transition>
 </tractor>
</mlt>
"""

TITLE.write_text(TITLE_XML, encoding="utf-8")
PROJECT.write_text(PROJECT_XML, encoding="utf-8")
print(f"wrote {PROJECT}")
print(f"wrote {TITLE}")
