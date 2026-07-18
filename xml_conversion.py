import xml.etree.ElementTree as ET
import os

classes = ["UAV"] # your class names, in order

# EDIT THESE: your folder paths
xml_dir = "/Users/rinzler/Desktop/train_new"      # folder containing your .xml files
out_dir = "/Users/rinzler/Desktop/Code_Practice/Drone Tracker/dataset/labels/train"           # folder where .txt files will be saved

os.makedirs(out_dir, exist_ok=True)

def convert_xml_to_yolo(xml_path, out_dir):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    w = int(root.find("size/width").text)
    h = int(root.find("size/height").text)

    lines = []
    for obj in root.findall("object"):
        cls = obj.find("name").text
        cls_id = classes.index(cls)
        box = obj.find("bndbox")
        xmin, ymin = float(box.find("xmin").text), float(box.find("ymin").text)
        xmax, ymax = float(box.find("xmax").text), float(box.find("ymax").text)
        
        xc = (xmin + xmax) / 2 / w
        yc = (ymin + ymax) / 2 / h
        bw = (xmax - xmin) / w
        bh = (ymax - ymin) / h
        lines.append(f"{cls_id} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")
    
    name = os.path.splitext(os.path.basename(xml_path))[0]
    with open(os.path.join(out_dir, name + ".txt"), "w") as f:
        f.write("\n".join(lines))

# Loop through every XML file in xml_dir
count = 0
for filename in os.listdir(xml_dir):
    if filename.endswith(".xml"):
        convert_xml_to_yolo(os.path.join(xml_dir, filename), out_dir)
        count += 1

print(f"Converted {count} XML files to YOLO format in '{out_dir}/'")