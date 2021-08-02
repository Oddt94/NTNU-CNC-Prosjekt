import ezdxf


# file_Contours = open("main_copytst2_contours.txt", "r")
# for x in file_Contours:

#  print(x)
line_color = {'color': 7}

point_m = 0
point_n = 0

point_0 = (155, 53)
point_1 = (462, 500)
point_2 = (769, 52)

# For en eller anan grunn da kjem trekanten oppned....hmm

# Create a new DXF document.
doc = ezdxf.new(dxfversion='R2010')

# Create new table entries (layers, linetypes, text styles, ...).
doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})

# DXF entities (LINE, TEXT, ...) reside in a layout (modelspace,
# paperspace layout or block definition).
msp = doc.modelspace()

# Add entities to a layout by factory methods: layout.add_...()
msp.add_line(point_0, point_1, line_color)
msp.add_line(point_1, point_2, line_color)
msp.add_line(point_2, point_0, line_color)
msp.add_text(
    'Table Test',
    dxfattribs={
        'layer': 'TEXTLAYER'
    }).set_pos((0, 0.2), align='CENTER')

# Save DXF document.
doc.saveas('test.dxf')

# file_Contours.close()
