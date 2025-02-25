# String Slicing

It's a technique to extract part of the string (text). Doing parallel with "Excel", we can say it's the same function: right, left and mid.

![image](https://github.com/user-attachments/assets/cf15ba09-c427-4ceb-90d3-b59221e8721d)

It will become clearer with the examples.

![image](https://github.com/user-attachments/assets/98f3ea96-61e1-4d9d-b462-5a57d4dee706)

### Documents:
- https://docs.python.org/pt-br/3/library/string.html
- https://docs.python.org/pt-br/3/library/stdtypes.html#textseq

**Example 01:** Variable name = [start]

```
name = "Diana Floriano Silva"
name[2] # Result: "a"
```

Why the letter "a"? Because the counting start in 0 (zero).

![image](https://github.com/user-attachments/assets/460c3a62-1367-4850-b7a6-d37090c802f6)

Look image above, space enters the calculation.

**Example 02:** Variable name = [:stop]

When it's not include argument "start", tools understands that it starts from the first character.

```
name = "Diana Floriano Silva"
name[:10] # Result: "Diana Flor"
```

**Example 03:** Variable name = [start:]

When it's not include argument "stop", tools understands that stop is at the end, in the last character.

```
name = "Diana Floriano Silva"
name[10:] # Result: "ano Silva"
```

**Example 04:** Variable name = [start:stop]

When it's included arguments "start" and "stop", tools understands it was determinded what caracter start and end.

```
name = "Diana Floriano Silva"
name[5:10] # Result: " Flor"
```

**Example 05:** Variable name = [start:stop:step]

When it's included arguments "start","stop" and "step", tools understands it was determinded what caracter start and end. Furthermore, determine the jumps the reading.

```
name = "Diana Floriano Silva"
name[5:10:2] # Result: " lr"
```

![image](https://github.com/user-attachments/assets/ea47a52d-7625-4c3b-bdf3-c9fa6ab5829e)


**Example 06:** Variable name = [:]

When it's not included any arguments, tools understands return it will be full.

```
name = "Diana Floriano Silva"
name[5:10:2] # Result: "Diana Floriano Silva"
```


**Example 07:** Variable name = [-start:-stop:-step]

When it's included negative arguments, tools understands return it will be of the right to left inverted.

```
name = "Diana Floriano Silva"
name[-1] # Result: "avliS onairolF anaiD"
```
![image](https://github.com/user-attachments/assets/57f16711-900b-4aa7-82b6-66793fd6e999)

In this case, follow the same standard to "start", "stop" and "step". Try to use this form.
