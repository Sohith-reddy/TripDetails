"""Build every trip-plan PDF into ../PDFs.  Run:  python3 scripts/build_all.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "..", "PDFs")

import overview, plan1, plan2, plan3, plan4, plan5  # noqa: E402

TARGETS = [
    (overview, "00_Overview_Trains_Flights_Gear_Budget.pdf"),
    (plan1, "01_Plan1_Standard_Shimla_Manali.pdf"),
    (plan2, "02_Plan2_Offbeat_Shimla_Manali_Jibhi_Tirthan.pdf"),
    (plan3, "03_Plan3_Kashmir_Winter_Gulmarg_Sonamarg_Pahalgam.pdf"),
    (plan4, "04_Plan4_Sikkim_Gangtok_SilkRoute_Pelling_Darjeeling.pdf"),
    (plan5, "05_Plan5_Uttarakhand_Rishikesh_Chopta_Tungnath_Auli.pdf"),
]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    os.makedirs(OUT, exist_ok=True)
    for mod, name in TARGETS:
        if only and mod.__name__ not in only:
            continue
        path = os.path.abspath(os.path.join(OUT, name))
        mod.build(path)
        print("built", path)
