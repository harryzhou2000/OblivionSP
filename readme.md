# Fictional Stealth VTOL Fighter HF-12 Oblivion


**WARNING**

**MAKE SURE YOU HAVE GONE THROUGH THE FLIGHT MANUAL (at least part 2.1. and 2.2.) BEFORE FLYING**

[GitHub Repo page](https://github.com/harryzhou2000/OblivionSP) illustrate the same document but with better formatting. The table of functions in 3. is formatted correctly there.


## 1. HF-12 Oblivion
![](https://i.postimg.cc/d3KjbLJ6/MainView.jpg)

HF-12 is my fictional multi-role stealth fighter with a canard-wing configuration. The Oblivion variant of HF-12 has diamond wings, VTOL capability and a fully functional cockpit. Features are as below:

### 1.1. VTOL
![](https://i.postimg.cc/xjRmfs5n/VTOL.jpg)
VTOLing is gf great importance. With the twin engine equipped with 90-degree deflecting capabilities and twin lift fans, the Oblivion can hover anywhere you like. With RCS and thrust linked to flight control, the Oblivion can easily maintain a fixed altitude and level attitude without your interference.

### 1.2. Thrust Vectoring
![](https://i.postimg.cc/15SZHB1n/Vector.jpg)
Experiencing 100° AoA? The vector nozzles can help you! The vector nozzles provide control forces for pitch, yaw and roll, merged into the common control logics.

### 1.3. Armament
![](https://i.postimg.cc/m2kvZgMj/Loadout.jpg)
All external weapons, including twin 30mm cannons and 4 bombs are configured to maintain best stealth performance, while the internal 8 AAMs and 2 AGMs can handle most situations.

### 1.4. Avionics
This aircraft supports GPS navigation, customizable waypoint, autopilot and a **HUGE** HUD. I feel F-22's HUD's too small while F-35's high-tech helmet's too complicated, so I used a **HUGE** HUD.

### 1.5. Cockpit
This is too complicated. I shall Explain in 2.

## 2. Flight Manual

All units are nautical.

### 2.1. Conventional Takeoff and Landing
The front gear is short causing a minus AoA in taxiing, so you must activate **AC4** for *vector nozzles* to gain extra pitch torque.

**LandingGear** is bond to flaps, and flying under 300 kts is tricky due to some bad features of the flaps, so take care and mind the speed when landing.

### 2.2. Level Flight
During level flight, the flight control always tries to help you maintain a steady attitude when the stick is not touched, and limits AoA for safety. So mostly trimming is useless for FC calculates the compensation automatically. If you are a fan of *stalled manuevers*, try the **Unleash AoA** button in the cockpit, which is described later. Make use of vector nozzles when stalled.

The Oblivion is capable of supersonic cruising, and the *afterburner* with **AC5** is able to boost it to Ma 3. The controls might be a bit of shaky over 2000 kts, but the aircraft is generally stable.

### 2.3. VTOL, and Hovering
VTOL mode is activated through **AC1**. Toggling VTOL is safe on the ground, but must be carefully treated in flight.

To takeoff:
1. **AC1** activate, **VTOL** max, then throttle 100%, after which you will enter an vertical ascension. You can choose to hover here. 
2. Then **VTOL** to 0, while pulling the stick a bit (or tapping S on PC), keeping the PitchAngle to be around +5°. Here you gain horizontal speed.
3. When IAS reaches above 250 kts, when you fly level, check that **VTOL** is indeed at 0 position, deactivate **AC1**, then you enter level flight.

You can retract landing gears anytime you like, but any premature deactivation of **AC1** will cause you to lose all control.

To hover:
Just fly like a helicopter. 
Note that when **AC1** is on and **VTOL** is max, when throttle is between *60%* and *80%*, the FC **automatically maintains a 0 climb rate**, and between *40%* and *60%* the FC **automatically maintains safe descending rate**. So if you plan to maintain altitude, put the throttle to 60-80%.

To land:
1. Fly level at around 350 kts, approach the landing field, then activate **AC1** and quickly **VTOL** max. Here you enter a stable glide.
2. Pull the stick hard to reduce speed, meanwhile put throttle into 60-80% to stabilize altitude. Reach a steady hovering.
3. Put throttle into 40-60% to get a controlled descending, and adjust horizontal position to aim the landing pad.

### 2.4. Weapons
Use weapons in the ordinary ways. Note that the Boom50 s are at high explosion scale (like a multi-hundred-ton tactical nuke) and you better stay away from the hit-point. **AC2** opens the weapon bay, but it is not mandatory when you fire, for the doors open anyway.

**AC7** jettisons all external hard-points and all weapons on them. Use if you want some electromagnetic stealth...

### 2.5. Cockpit, Autopilot and Waypoints

#### 2.5.1. Cockpit Layout

All the units in cockpit are nautical except unit is shown, i.e. altitude in feet, speed in knots, and range in nautical miles.

The illustrative markings in the images represent:
1. Yellow Rectangles and Text: Regions that display some information, screen or HUD. 
2. Red Text: show the meaning of components being not so obvious to understand. (which means other buttons are decoration.)
3. Blue Rectangles and Text: Regions that contain functional buttons or triggers.
4. Purple Text: show functions of lever-likes or specific keys. 

##### 2.5.1.1. Mid Part
The mid part of cockpit (right click open to get large image):
![](https://i.postimg.cc/sx7jDPvk/Cockpit-Mid.png)
(Note the tilted texts are in the HUD or LCD screen, not markings.)

The HUD and screen are easy to understand. Of the 4 sections of screen:
 - *Aircraft Section* shows data of the plane, the little plane sketch is connected to status of control surfaces, gears and nozzles; 
 - *Weapon Section* shows locking and weapon stock status; 
 - *Autopilot Section* shows currently settings for autopilot; 
 - *Map Section* shows a tactical map containing relative positions of *Selected Target*, *Custom Waypoint*, and *Places of Interest*. The target uses code *TGT* and Waypoint *WPT*. The POIs: *WRT* for Wright Airport, *SPK* for Skypark, *BDT* for Bandit Airport, *YGR* for Yeager Airport, *AVL* for Avalanche Airport, *MWR* for Maywar.

The 3 button regions on the top can be easily understood reading the label or tip. The Num Pad's usage is explained later.

##### 2.5.1.2. Right Part
The right part of cockpit (right click open to get large image):
![](https://i.postimg.cc/J4w7dhns/Cockpit-Right.png)

The Engines screen is absolutely useless, just for some decoration.

The top-3 buttons in *External-Nav-Map* are easy to understand:
 - **ULS AoA** Turn of the AoA limit, to start some stalling...
 - **Canopy** == **AC6**, open or shut the glass-shiny-sleek fairing over you head.
 - **Fold Wings** For storage on aircraft carriers, should only work on land.
The second and third row are Nav and Map buttons which are explained later.
Bottom row is decoration.

In the *Autopilot* buttons, the rightmost column is dummy decoration, and others are
explained later.

##### 2.5.1.3. Left Part
The right part of cockpit (right click open to get large image):
![](https://i.postimg.cc/L8Q8D3Zp/Cockpit-Left.png)

*All Weapons Section* is just in case you install any other 'unofficial' weapon, and *Weapon Bay* is almost a decoration.

*AC Triggers* directly controls activation groups. But apart from **AC3** Ejection, all other Activation Groups can be controlled somewhere else in the cockpit.

#### 2.5.2. Navigation
You can set a customized waypoint on the *Map*, if you know the latitude & longitude in the scene. Here are the steps (assuming you are bound to go to Kraken (74429,97344)):
1. Goto the *External-Nav-Map Button Region*, press **NAV** to activate navigation mode, then the waypoint is shown, but is set to (0,0), which can be seen below the *Map*.
2. Press **Set Lat**, so that it is 'on' (being pressed down), then type 74429 in the **Num Pad**. You can see what you have type in the small screen at the top of **Num Pad**. If you got it wrong, use **DEL** to delete last digit, or use **C** to clear all. Finally, press the **Enter** in **Num Pad** to send the buffer to the latitude setting, then '74429' should appear on the waypoint information below *Map*. Last, **Deactivate** the **Set Lat** button, so that further operations do not affect the latitude setting.
3. Use button **Set Lon** and **Num Pad** to do the same for longitude (enter 97344). (Note: if you want to type a negative number, use **-** button in **Num Pad** to toggle the sign of the num pad buffer.)

Here, your way point is where you want to be, and you can see where it is on the *Map*.

#### 2.5.3. Autopilot
You can use **HOLD XXX** in *Autopilot Button Region* to hold altitude, speed (GS) or heading or any combination of them. The current setting value is shown on the *Autopilot Region* of the middle screen. To change them, you can:
- Press once **CUR XXX** in *Autopilot Button Region* to set the value to current flight data (where XXX can be ALT, SPD or HDG), or 
- Toggle on the button **SET XXX** to manually set the value with **Num Pad** like in 2.5.2. Remember to toggle of that **SET XXX** after finishing the manual setting.

Note that autopilot is off if you are far from level, you must have less than 45° of pitch and roll to enter autopilot.

You can still control the attitude a bit when autopilot is on. Let go of stick to let autopilot do right.

When navigation mode is on, you can not set the autopilot target heading, for it is always overwritten by the waypoint's heading.

#### 2.5.4. Map Zooming
The map has variable zooming levels, and a length legend is shown on the map to mark the real distance. To change zooming, tap buttons **Zoom +** and **Zoom -** in *External-Nav-Map Button Region*, and reset it with **Zoom RST**.

The objects out side the map region are collapsed on the boundary, being dimmer than normal.

#### 2.5.5. Ejection
Tired of sitting in the cockpit? Use **AC3** to toss yourself (or the seat actually) out! Use camera 'Seat' to gain a 3rd person view of ejection.

## 3. List of Functions

All bold names are activation groups or button names (labels), or any SP UI operation or axis input. Italic names are button region names (blue) shown in the images of cockpit.

SP page doesn't handle this table well (not standard markdown), but github should do. See the same document with the table here:
https://github.com/harryzhou2000/OblivionSP

|Location|Function|
|---|---|
|**AC1**==**VTOL** in *Engines*|Toggle VTOL Mode|
|**AC2**==**WPN BAY** in *Target*|Toggle Weapon Bay Door|
|**AC3**|Eject|
|**AC4**==**VEC NOZ** in *Engines*|Toggle Vector Nozzles|
|**AC5**==**ABN** in *Engines* == **ABN** near throttle|Toggle Afterburner|
|**AC6**==**Canopy** in *External-Nav-Map*|Toggle Canopy|
|**AC7**==**TOSS HDP** in *Misc*|Jettison Hard-points|
|**AC8**==**Beacon** in *Misc*|Toggle Lights|
|**ActivateCatapult**==**Catapult** in *Misc*|Link Catapult|
|**Launch Countermeasures**==**Flare** in *Misc*|Launch Countermeasures|
|**Previous/Next Weapon**==**PREV/NEXT WPN** in *Target*|Prev/Next Weapon Selection|
|**Cycle Targeting Mode**==**TGT MODE** in *Target*|Cycle Targeting Mode|
|**0-9** in *Num Pad*|Enter a digit into buffer|
|**DEL** in *Num Pad*|Delete last digit|
|**C** in *Num Pad*|Clear all digits|
|**-** in *Num Pad*|Flip buffer's sign|
|**Ender** in *Num Pad*|Send buffer to all active setting|
|**ULS AoA** in *External-Nav-Map*|Toggle AoA limiting|
|**Fold Wing** in *External-Nav-Map*|Fold wings|
|**NAV** in *External-Nav-Map*|Toggle waypoint navigation mode|
|**SET LAT** in *External-Nav-Map*|Set waypoint latitude for receiving num pad's buffer|
|**SET LON** in *External-Nav-Map*|Set waypoint longitude for receiving num pad's buffer|
|**Zoom +/-** in *External-Nav-Map*|Adjust Map zooming|
|**Zoom RST** in *External-Nav-Map*|Reset Map zooming to original|
|**Hold XXX** in *Autopilot*|Open autopilot for XXX, XXX={ALT,SPD,HDG}|
|**SET XXX** in *Autopilot*|Set XXX setting for receiving num pad buffer, XXX={ALT,SPD,HDG}|
|**CUR XXX** in *Autopilot*|Set XXX setting as current status, XXX={ALT,SPD,HDG}|
|**X** near throttle|Set throttle to 0|
|**O** near throttle|Set throttle to Max|

**VTOL** only controls VTOL with **AC1**, **Trim** only controls pitch trim.
**Roll** **Yaw** **Pitch** **Throttle** are what they are supposed to do. Note that throttle's behavior differs slightly in hovering, see 2.3.


## 4. Label Generation and Variable Coding

This one-piece HUD's label contains over 50kB data, and the map likewise. I certainly didn't code it by hand, the python code can also be found here:
https://github.com/harryzhou2000/OblivionSP

There are nearly 90 variables in the project, so they are divided by 'Comment' variables that describe the following section.

## 5. Credit

HUD generating methodology based on [1Parts HUD](https://www.simpleplanes.com/a/0dH9ML)
Ejection warning sign from [Fc-912C](https://www.simpleplanes.com/a/e6zXvN/Fc-912C)


## Why I made this

HF-12 was an old design of mine years ago, but gradually renewed as the game updates. In the past year of 2021, I haven't played SP much, but so I missed most of the fancy updates. As soon as I was aware of the exciting new features, I started working on the cockpit and flight controls, and the outcome of 40 hrs of work is Oblivion.