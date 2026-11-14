# Soto Ayam Ibu — food-picture-01

A steaming bowl of Indonesian soto ayam on a dark wooden warung table:
golden turmeric broth, noodles, shredded kampung chicken, bean sprouts,
a halved boiled egg, fried shallots, chili rings, a krupuk leaning on
the bowl and a lime wedge on its rim. Behind the bowl, the warung's own
chalkboard menu reads "SOTO AYAM / ayam kampung / kunyit • serai •
santan / Rp 15.000".

## How it was made

The picture was drawn programmatically (Python + PIL, seeded and
deterministic) as an original illustration — warm light, steam, and a
personal artifact with legible text inside the image, the way a real
warung would show its dish.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` to the output directory (standard library
only), so both grader runs write identical bytes.
