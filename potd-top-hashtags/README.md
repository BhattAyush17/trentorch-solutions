# TOP HASHTAGS

Beginner | nlp

**Difficulty:** Easy
**Tags:** NLP

---

### Story

TikTok's hashtag-suggestion model needs a vocabulary built from raw captions before it can suggest
anything: take the `k` most frequent hashtags, everything else becomes `<unk>`.

---

### The Problem

Count hashtag frequency across all captions; return the top `k` by count, ties broken by earliest
first appearance in the input.

### Input Format

```
k
n
caption_1
...
caption_n
```

Hashtags are whitespace-separated tokens starting with `#`; non-hashtag words are ignored.

### Output Format

`k` lines (fewer if fewer than `k` distinct hashtags exist): `hashtag count`.

### Constraints

- `1 <= k <= 1000`, `1 <= n <= 10^4`
- Time limit: 1.0 second.

---

### Example

**Input**

```
2
1
#fyp #dance #fyp #comedy #fyp #dance #viral
```

**Output**

```
#fyp 3
#dance 2
```
