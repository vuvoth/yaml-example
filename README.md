# Scalar type

```yaml
- interger: 2
- float: 2.3
- string1: "vu vo thanh"
- string2: chamw
- boolean: true
- date: 2019-12-01 # data type
```

# Sequences

```yaml
candys:
  - beans
  - lollipop
  - hard candy
  - you
```

# Hashes (Key - Value)

```yaml
Vu:
  fullname: Vu Vo Thanh
  job: Blockchain Dev and AI research
  salary: 50000 usd / month
  skills:
    - sleep
    - eat
    - make my crush have boyfriend
```

# Heredocs

## Block notation: Newlines become to spaces

```yaml
content: What i've felt
  What i've know
  Never shined through in what I've shown
  Never be
  Never see
  Won't see what might have been
```

We will get

```json
{
  "content": "What i've felt What i've know Never shined through in what I've shown Never be Never see Won't see what might have been"
}
```

## Literal style: Newlines are preserved

```yaml
content: |
  What i've felt
  What i've know
  Never shined through in what I've shown
  Never be
  Never see
  Won't see what might have been
```

we will get

```json
{ "content": "What i've felt\nWhat i've know\nNever shined through in what I've shown\nNever be
\nNever see\nWon't see what might have been\n" }
```

## Folded style: folded newlines are preserved

```yaml
content: >
  What i've felt
  What i've know
  Never shined through in what I've shown
  Never be
  Never see
  Won't see what might have been
```

We get

```json
{
  "content": "What i've felt What i've know Never shined through in what I've shown Never be Never see Won't see what might have been\n"
}
```

# Aliases

```yaml
# Use & for create refer
# Use * for use refer
# Use in same hash

items:
  - &banana
  - *banana

---
#Use in another hash use "<<: *ref"
base: &base
  name: Everyone has same name

foo: &foo
  - *base
  - age: 10

bar: &bar
  <<: *base
  age: 20

baz: *base
```
