<template>
  <div class="page-grid">
    <section class="panel">
      <div class="panel-header">
        <h4>System Overview</h4>
      </div>
      <p class="section-copy">
        This project is designed for AI undergraduate graduation project demonstrations. The front
        end focuses on polished interaction and visual presentation, while the back end exposes a
        lightweight API that can be upgraded to a real inference pipeline.
      </p>
      <el-descriptions :column="1" border>
        <el-descriptions-item label="Architecture">Frontend / Backend Separation</el-descriptions-item>
        <el-descriptions-item label="Frontend">Vue 3, Vite, Element Plus, Axios, Router, Pinia</el-descriptions-item>
        <el-descriptions-item label="Backend">FastAPI, Uvicorn, Pydantic</el-descriptions-item>
        <el-descriptions-item label="Deployment">Vercel + Render / Railway / Docker</el-descriptions-item>
      </el-descriptions>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h4>Defense Presentation Highlights</h4>
      </div>
      <ul class="feature-list">
        <li>Modern dashboard with strong visual hierarchy for project defense scenarios.</li>
        <li>Image upload and API connectivity demonstrate end-to-end integration capability.</li>
        <li>Structured JSON results make it easy to extend into YOLO, OCR, or custom CV models.</li>
        <li>Separate deployment strategy supports rapid student delivery and future expansion.</li>
      </ul>
    </section>
  </div>
</template>

