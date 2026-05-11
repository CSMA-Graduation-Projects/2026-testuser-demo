<template>
  <div class="app-shell">
    <aside class="side-panel">
      <div>
        <p class="eyebrow">AI Graduation Demo</p>
        <h1>AI-Powered Undergraduate Graduation Project Demo</h1>
        <p class="lead">
          A modern, presentation-ready front-end and back-end template for undergraduate AI
          graduation projects.
        </p>
      </div>

      <el-menu
        :default-active="route.path"
        class="nav-menu"
        router
        background-color="transparent"
        text-color="#c8d7ff"
        active-text-color="#ffffff"
      >
        <el-menu-item index="/">Dashboard</el-menu-item>
        <el-menu-item index="/upload">Image Upload</el-menu-item>
        <el-menu-item index="/result">AI Result</el-menu-item>
        <el-menu-item index="/about">System Intro</el-menu-item>
      </el-menu>

      <div class="side-footer">
        <span>Vue 3 + FastAPI</span>
        <span>Defense Ready UI</span>
      </div>
    </aside>

    <main class="main-panel">
      <header class="topbar">
        <div>
          <p class="topbar-label">Project Workspace</p>
          <h2>{{ route.meta.title }}</h2>
        </div>
        <el-tag effect="dark" type="success">Live Demo Template</el-tag>
      </header>

      <section class="content-card">
        <RouterView />
      </section>
    </main>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

