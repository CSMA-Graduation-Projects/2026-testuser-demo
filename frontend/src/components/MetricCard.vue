<template>
  <article class="metric-card">
    <p>{{ label }}</p>
    <strong>{{ value }}</strong>
    <span>{{ description }}</span>
  </article>
</template>

<script setup>
defineProps({
  label: { type: String, required: true },
  value: { type: String, required: true },
  description: { type: String, required: true }
})
</script>

