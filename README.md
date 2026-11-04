# North India Winter Trip: 24 Dec 2026 – 3 Jan 2027 (6 people)

Leave Hyderabad 24 Dec, home by 3 Jan. Budget ₹25–30k per person. Stays on Airbnb. Shimla is reached by the Kalka toy train.

## The PDFs (in `PDFs/`)

| File | Plan | Per person, 6 sharing (shoestring / recommended) |
|---|---|---|
| `00_Overview_All_Plans_Trains_Airbnb_Gear.pdf` | All plans compared; trains from Hyderabad, Kazipet, Warangal and Vijayawada; Delhi → Kalka → toy train connections; return trains; flights; vehicles for 6; Airbnb approach; international options checked; winter gear | n/a |
| `01_Plan1_Standard_Shimla_ToyTrain_Manali.pdf` | Toy train to Shimla, Kufri, Narkanda–Hatu, Manali, Solang, Atal Tunnel–Sissu, Naggar, Sethan, Kasol | ₹23.7k / ₹32.3k |
| `02_Plan2_Offbeat_Shimla_Narkanda_Jibhi_Sethan.pdf` | Toy train, Mashobra, Shali Tibba, Narkanda, Thanedar, Jalori, Jibhi, Tirthan, Sethan NYE | ₹22.5k / ₹29.9k |
| `03_Plan3_Kashmir_Winter_by_Train.pdf` | Jammu–Srinagar Vande Bharat, Gulmarg, Drung, Doodhpathri, Sonamarg, Pahalgam–Aru | ₹22.3k / ₹29.6k |
| `04_Plan4_Sikkim_Gangtok_SilkRoute_Darjeeling.pdf` | Gangtok, Tsomgo–Nathula, Silk Route, Aritar, Ravangla, Pelling, Rinchenpong, Darjeeling (flights) | ₹33.8k / ₹43.5k (lean ≈ ₹29–31k) |
| `05_Plan5_Uttarakhand_Rishikesh_Chopta_Auli.pdf` | Rishikesh, Deoria Tal, Tungnath–Chandrashila, Auli–Gorson, Haridwar | ₹20.7k / ₹29.1k |
| `06_Plan6_Amritsar_Dalhousie_Dharamshala_Bir.pdf` | **New:** Golden Temple, Wagah, Dalhousie–Khajjiar, McLeodganj–Triund, Palampur, Bir, Kangra toy train | ₹19.2k / ₹29.0k |
| `07_Plan7_Kinnaur_Winter_by_ToyTrain.pdf` | **New:** toy train both ways, Narkanda, Sarahan, Sangla, Kalpa, Nako, Shimla NYE | ₹21.4k / ₹28.1k |
| `08_Plan8_Nepal_Overland_International.pdf` | **New, international:** weekly Hyderabad–Raxaul train (Thu 24 Dec), Kathmandu, Bandipur, Pokhara street festival, back via Patna | ₹18.8k / ₹28.2k |

Budget totals are computed from each plan's itemised table by `scripts/build_all.py`, so the README, overview and plan pages match.

Each plan has:
- how to get there and back (including Kazipet/Warangal/Vijayawada boarding where it helps)
- the cheapest connecting trains, with buffers based on the train timings
- a day-by-day itinerary with spend per person
- Airbnb best-rated and budget picks for every stop
- vehicles for 6, bike/scooty rentals
- winter gear rental points
- an itemised budget, what to book now, a Plan B, and sources

## Book first (as of 4 Nov 2026)

1. **Return train for 2 Jan:** 12724 Telangana Exp (New Delhi 16:00 → Hyderabad ~17:10, 3 Jan). The 60-day window opened 3 Nov.
   For Nepal, book **17005 Hyderabad–Raxaul for Thu 24 Dec** (weekly) and **12792 Danapur–Secunderabad for 2 Jan**.
2. **Onward train for 24 Dec:**
   - Default: 12723 Telangana Exp, Hyderabad Deccan 06:00.
   - Fast option: 12621 Tamil Nadu Exp from Kazipet 06:55 / Warangal 06:50 / Vijayawada ~04:00.
   - Then the 25 Dec connection (12311 Kalka Mail / 14033 Jammu Mail / Amritsar train) and the 26 Dec toy train.
3. **NYE Airbnbs (30 Dec–1 Jan)** with flexible cancellation.

General quota allows 6 passengers per PNR; Tatkal allows only 4, so Tatkal needs 2 bookings.

## Caveats

- Reddit, IRCTC, ConfirmTkt, erail and Airbnb pages could not be opened from the research environment. Train timings, Airbnb ratings and prices
  come from search results across several sites. Seat availability and live Airbnb prices were not checked; the "Dec price for 6" column is an estimate.
- Some train running days and timings conflict between sources; they are marked "verify". Confirm on IRCTC / NTES before paying.

## Rebuilding the PDFs

```bash
pip install reportlab   # uses DejaVu fonts from /usr/share/fonts/truetype/dejavu
python3 scripts/build_all.py
```

Shared trains, toy train, vehicle, Airbnb and gear tables are in `scripts/shared.py`; each plan is in `scripts/planN.py`.
