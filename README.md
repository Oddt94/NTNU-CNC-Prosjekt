# NTNU-CNC-nesting 

Setting up a 2-axis CNC machine for nesting.

The idea is to set up a camera above the work table and use opencv to identify edges from raw material (sheet to be cut), material type and material thickness. Identified edges will be converted to vector format and imported into a nesting module. Cutting files (dxf, svg, etc.) will be loaded from a file share into the same nesting module. Ideally the process of placing sheets on the work table, nesting and preparing g-code for cutting will be almost in realmtime. Cutting data and speeds will also be set automatically.
