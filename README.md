# NTNU-CNC-nesting 

Setting up a 2-axis CNC machine for nesting.

The idea is to simplify the process of cutting material by using a camera. A camera is placed above the work table and using opencv to identify edges from raw material (sheet to be cut), material type and material thickness. Identified edges will be converted to vector format and imported into a nesting module. Cutting files (dxf, svg, etc.) will be loaded from a file share ont the produciton server into the same nesting module. Ideally the process of placing sheets on the work table, nesting and preparing g-code for cutting will be almost in realmtime. Cutting data and speeds will also be set automatically based on identified material from the camera.

Current state of the project:
- Program takes camera input and outputs a svg file with contour data.
- The contour data has been scaled from camera coordinates to coordinates on the work plane using homography
- A program has been created to get camera coordinates from clicking on the screen, this is used on a set of calibration plates to create the homography matrix.
- Converting svg files to readable gcode

Problems and what is left of the project:
- Building in auto nesting into the software, currently using external resources to accomplish task, 
  this is a possible source of a y-directional offset that we have not resolved yet, so we are hoping that changing to internal nesting will solve this issue
  (see https://github.com/Ultimaker/pynest2d for a potential solution)
- Creating an automated way of reading in parts from both dxf and svg files from a shared folder
  these parts also need to be scaled to be scaled correctly in mm to fit into the sheet model.
- Transferring gcode to CNC machine system (an example file for transferring gcode over serial to a grbl enable machine is included)

Suggested features/benefits:
1. Simplifies the use of left over materials. Non-rectangular plates with holes and cut-outs can easily be used.
2. Plates can be placed on the cut table with random orientation.
3. Several plates can be placed on the same cutting table.
4. Easier to implement automatic material handling. Both pulling material from plate magazine and picking cut parts from the table.
5. Enables use of conveyor belts.
6. Live nesting data and cutting parts are projected onto the plates by a mini projector. Enables preview of cutting. 
