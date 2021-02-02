<template>

    <button
        class="btn  blue-btn  btn-block"
        :class="{ 'is-loading': status }"
        type="submit"
    >
        <div class="text">
            {{ text }}
        </div>
        
        <div class="loading-icon">
            <i class="fa fa-cog fa-spin"></i>
        </div>
    </button>
        
</template>

<script>

export default {
  name: "loader-button",

  props: {
    status: {
      type: Boolean,
      required: true
    },

    text: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped>

    button > .text {
        will-change: transform, opacity;
        transition: all 0.3s ease-in-out;
        opacity: 1;
    }
    button > .loading-icon {
        position: absolute;
        left: 0;
        right: 0;
        transition: all 0.3s ease-in-out;
        will-change: transform, opacity;
        opacity: 0;
    }
    button.is-loading > .text {
        transform: translateY(-100px);
        opacity: 0;
    }
    button.is-loading > .loading-icon {
        transform: translateY(-100%);
        opacity: 1;
    }
</style>
