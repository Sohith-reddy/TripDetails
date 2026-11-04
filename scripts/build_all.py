"""Build every trip-plan PDF into ../PDFs.  Run:  python3 scripts/build_all.py"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.abspath(os.path.join(HERE, "..", "PDFs"))

import overview, plan1, plan2, plan3, plan4, plan5, plan6, plan7, plan8  # noqa: E402

PLANS = [
    (1, plan1, "01_Plan1_Standard_Shimla_ToyTrain_Manali.pdf"),
    (2, plan2, "02_Plan2_Offbeat_Shimla_Narkanda_Jibhi_Sethan.pdf"),
    (3, plan3, "03_Plan3_Kashmir_Winter_by_Train.pdf"),
    (4, plan4, "04_Plan4_Sikkim_Gangtok_SilkRoute_Darjeeling.pdf"),
    (5, plan5, "05_Plan5_Uttarakhand_Rishikesh_Chopta_Auli.pdf"),
    (6, plan6, "06_Plan6_Amritsar_Dalhousie_Dharamshala_Bir.pdf"),
    (7, plan7, "07_Plan7_Kinnaur_Winter_by_ToyTrain.pdf"),
    (8, plan8, "08_Plan8_Nepal_Overland_International.pdf"),
]
OVERVIEW = "00_Overview_All_Plans_Trains_Airbnb_Gear.pdf"

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    keep = {OVERVIEW} | {name for _, _, name in PLANS}
    for old in glob.glob(os.path.join(OUT, "*.pdf")):
        if os.path.basename(old) not in keep:
            os.remove(old)
    totals = {}
    for num, mod, name in PLANS:
        totals[num] = mod.build(os.path.join(OUT, name))
        print(f"built {name}: shoestring ₹{totals[num][0]:,} / recommended ₹{totals[num][1]:,}")
    overview.build(os.path.join(OUT, OVERVIEW), totals)
    print("built", OVERVIEW)
