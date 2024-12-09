text ← •file.Lines "./OCTO-Coding-Challenge-2024-Week-1-Part-2-input.txt"
IsVowel ← {𝕩∊"aeiouyAEIOUY"}
IndexOfMax ← ⊑⊢⊐⌈´
•Show IndexOfMax(+´∘IsVowel¨ text)