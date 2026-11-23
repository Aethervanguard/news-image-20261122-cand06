# A Black Hole Outgrew Its Galaxy — news-image-20261122 candidate 6

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Aethervanguard/news-image-20261122-cand06/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Aethervanguard/news-image-20261122-cand06/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the [make.fun news-image-20261122 bounty](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122): sum up Sunday 22 November 2026 in one image.

## The image

Full-bleed minimalist layout: the JWST deep field fills the whole frame, darkened, with the headline "A Black Hole Outgrew Its Galaxy" overlaid (3.3-million-sun black hole in a galaxy 100 times too small, 12 billion years ago), a stat strip near the bottom, and an "Also today" strip (Iran strikes US bases in Bahrain, COP31 deadlocked, Russia's barrage on Kryvyi Rih, BepiColombo enters Mercury orbit).

## How it works

The grader runs bare-stdlib Python with no fonts and no network, so the image is rendered at build time (PIL) and shipped as `entry.png`. `main.py` (stdlib only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, byte for byte. Deterministic: two runs produce identical bytes.
