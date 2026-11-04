"""Section builders that several plan PDFs reuse."""
import shared as S

ONWARD_W = [0.2, 0.19, 0.16, 0.1, 0.18, 0.17]
RETURN_W = [0.2, 0.17, 0.18, 0.1, 0.13, 0.22]
FLIGHT_W = [0.18, 0.24, 0.12, 0.26, 0.2]


def pick(table, idx):
    return [table[0]] + [table[i] for i in idx]


def delhi_trains(d, onward_idx=(1, 2, 4, 7), return_idx=(1, 2, 3, 4), show_method=True):
    d.h2("Hyderabad → Delhi: trains that work for 24 Dec (early morning first)")
    d.table(pick(S.ONWARD_TRAINS, onward_idx), ONWARD_W)
    d.small(S.TELANGANA_HALTS)
    d.space(4)
    if show_method:
        d.callout("Waitlisted? Check every halt this way", S.HALT_METHOD[:5] + [S.HALT_METHOD[5]], "warn")
    d.h2("Delhi → Hyderabad: trains that get you home by 3 Jan")
    d.table(pick(S.RETURN_TRAINS, return_idx), RETURN_W)


def flights(d, idx, title="Flights from Hyderabad (to save 1–2 days)"):
    d.h2(title)
    d.table(pick(S.FLIGHTS, idx), FLIGHT_W)
    d.small(S.FLIGHT_NOTE)
    d.space(4)


def gear(d, local_rows):
    d.h1("Winter gear: what to buy, what to rent, and where")
    d.p(S.GEAR_SUMMARY)
    d.table(pick(S.GEAR_TABLE, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)), [0.2, 0.1, 0.2, 0.3, 0.2])
    d.h2("Rental points on this route")
    d.table(local_rows, [0.25, 0.45, 0.3])


def packing_and_safety(d, extra_safety=()):
    d.h2("Carry list")
    d.bullets(S.PACKING)
    d.h2("Safety &amp; buffers")
    d.bullets(list(S.COMMON_SAFETY) + list(extra_safety))
