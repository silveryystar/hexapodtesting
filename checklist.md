## Procedure Checklist
### Requirements
- [] M2: The detector focus range (Δz) shall be ≥ ±1 mm relative to predicted nominal best focus.
- [] M3: The detector focus resolution (δz) shall be ≤ 0.2 µm.
- [] M4: The detector focus repeatability shall be ≤ ±0.2 µm.
- [] M5: The FCS mechanism lateral range (independently of Δx and Δy) shall be ≥ ±225 µm.
- [] M6: The FCS mechanism lateral resolution (independently of δx and δy) shall be ≤ 0.5 µm.
- [] M7: The FCS mechanism lateral repeatability shall be ≤ ±0.5 µm.
- [] Measure and verify the angles roll, pitch, and yaw.

- M2 requirement is checked in **range0.py**.
- M3 requirement is checked in **resolution.py**.
- M4 requirement is checked in **repeatability.py**
- M5 requirement is checked in **range0.py**
- M6 requirement is checked in **resolution.py**.
- M7 requirement is checked in **repeatability.py**.

In order:
- **operational.py** checks operational testing, including homing.
- **coordinates.py** checks coordinate transformation.
- **range0.py** checks M2 and M5.
- **resolution.py** checks M3 and M6.
- **repeatability.py** checks M4 and M7.