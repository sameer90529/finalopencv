"""Streamlit UI Glassmorphism & KPI Component Builders"""
import streamlit as st

def render_metric_card(caption: str, number: str, hint: str, color: str = "#0F172A") -> str:
    return f"""<div class="metric-card">
<div class="metric-caption">{caption}</div>
<div class="metric-number" style="color: {color};">{number}</div>
<div class="metric-hint">{hint}</div>
</div>"""
