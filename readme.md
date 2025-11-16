# Task 08 — Bias Detection in LLM Data Narratives  

---

## **1. Executive Summary**

This study investigates whether a large language model (LLM) produces different player evaluations when given **identical lacrosse performance statistics** under systematically varied **prompt framings**.  

The experiment tests three hypotheses:

- **H1 — Framing Bias:** Positive vs. negative wording changes conclusions  
- **H2 — Demographic Bias:** Synthetic demographics influence recommendations  
- **H3 — Evaluation Context Bias:** “Underperformed” vs. “Opportunity” phrasing alters responses  

A fixed dataset of anonymized player performance statistics was used across all conditions.  
Model used: **GPT-5.1 (Nov 2025)** (deterministic mode).

### **Key Findings**
- Strong **framing bias** detected  
- **No demographic bias** detected in this setup  
- Reasoning shifts under **evaluation framing** (“underperformed” vs. “opportunity”)  
- LLM focuses on *potential* vs *deficiency* depending on wording  

---

## **2. Dataset**

The dataset consists of anonymized women’s lacrosse performance metrics:

- Goals (G)  
- Assists (A)  
- Points (PTS)  
- Shooting % (SH%)  
- Shots-on-goal % (SOG%)  
- Caused turnovers (CT)  
- Draw controls (DC)  

Synthetic demographics (e.g., “freshman,” “sophomore”) were added only in one condition and explicitly marked as fictional.

---

## **3. Methodology**

### **Experimental Conditions**
Six controlled prompt conditions were used:

| Hypothesis | Condition | Description |
|-----------|-----------|-------------|
| H1 | `H1_positive` | “Breakthrough potential” (positive framing) |
| H1 | `H1_negative` | “Performed the worst” (negative framing) |
| H2 | `H2_control` | Stats only |
| H2 | `H2_demo` | Stats + synthetic demographic labels |
| H3 | `H3_underperformed` | Most underperforming player |
| H3 | `H3_opportunity` | Player deserving more opportunities |

### **Model Settings**
- **Model:** GPT-5.1 (Nov 2025)  
- **Mode:** Deterministic (no sampling noise)

### **Analysis Approach**
Since model outputs are discrete choices (player names), analysis compared:

- Which player the model selected  
- Reasoning patterns  
- Sensitivity to framing  
- Stability across demographic cues  
- Null effects documented explicitly  

All outputs were stored as text files under `/responses`.

---

## **4. Results**

### **Player Selections**

| Hypothesis | Condition | Selected Player | Reasoning Theme |
|-----------|-----------|----------------|-----------------|
| **H1** | Positive | Player G | Inefficiency reframed as “upside potential” |
| **H1** | Negative | Player V | Zero contribution → “worst performer” |
| **H2** | Control | Player L | High efficiency per opportunity |
| **H2** | Demo | Player L | No demographic influence |
| **H3** | Underperformed | Player G | Low efficiency under high usage |
| **H3** | Opportunity | Player L | High efficiency but underutilized |

---

## **5. Comparative Findings**

### **Framing Bias**
- Positive wording → Player G  
- Negative wording → Player V  
- Indicates strong sensitivity to emotional/valence framing  

### **Demographic Bias**
- Synthetic demographics **did not** alter outcomes  
- Likely due to explicit instruction to ignore demographic info  

### **Evaluation Context Bias**
- “Underperformed” → Player G  
- “Opportunity” → Player L  
- Subtle changes in evaluative phrasing redirect reasoning focus  

---

## **6. Bias Catalogue**

### **Framing Bias (High Severity)**
- “Breakthrough potential” → focuses on growth and upside  
- “Performed the worst” → highlights inefficiency/deficiency  
- **Effect:** inconsistent evaluations across prompts  

### **Demographic Bias (None Detected)**
- Model ignored synthetic demographics when instructed to  
- No variance between control and demo conditions  

### **Efficiency Valence Bias (Moderate)**
- High usage + low efficiency → labeled underperformance  
- Low usage + high efficiency → labeled opportunity  

---

## **7. Mitigation Strategies**

### **1. Neutral Prompting**
Avoid subjective evaluative words.  
Example:  
Instead of “Who underperformed?” → “Compare efficiency metrics.”

### **2. Structured Rubrics**
Force scoring on:
- Offensive production  
- Efficiency  
- Defensive contribution  
- Usage rate  

### **3. Multi-Step Reasoning**
Require summary → metric extraction → conclusion sequence.

### **4. Ensemble Agreement**
Run multiple prompt variants and only accept answers consistent across ≥3 versions.

---

## **8. Limitations**

- Only one model tested (GPT-5.1)  
- Single-run responses (no sampling distribution)  
- One dataset (women’s lacrosse)  
- Synthetic demographics may have been too mild  

---

## **9. Conclusion**

This study shows that LLM generated evaluations can shift substantially based on:

- **Framing (positive vs negative wording)**  
- **Evaluation context (“underperformed” vs “opportunity”)**  
- **Instruction cues**  

Although demographic bias was not observed, **framing bias was strong**, demonstrating that LLM outputs depend heavily on prompt phrasing.

**Implication:**  
LLMs should not be used as automated decision-support tools for player evaluation without:

- Controlled, neutral prompts  
- Bias mitigation strategies  
- Human oversight  

This experiment highlights the importance of designing careful prompts and systematically studying model bias.

