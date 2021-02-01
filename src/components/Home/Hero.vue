<template>
    <div>
        <div class="hero-wrapper" id="hero">
            <div class="container">
                <div class="headline row px-3">
                    <div class="col-12 col-md-6">
                        <div class="text-center text-md-left">
                            <h1 class="heading mt-3">
                               AUN VENDOR
                            </h1>
                            <h2 class="md-3 font-weight-bold">
                                Welcome to AUN's Premier Online Market Place
                            </h2>
                            <h3 class="mt-5 text-justify text-faded">
                               We help you discover products and services you are looking for on
                               campus, and we help student entrepreneurs build successful
                               businesses. We are Marche! ✨
                            </h3>

                            <router-link 
                            :to="{ name: 'adverts' }"
                            class="btn call-to-action"
                            
                            >
                                Explore
                            </router-link>
                        </div>
                    </div>

                    <div
                    class="col-12 col-md-6 image text-left  mt-md-0 mt-5"
                    >
                        <div class="round-illustration">
                            <img
                                alt="College Students"
                                class="img-fluid"
                                src="../../assets/svg/home-hero-image.svg"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
    name: "Hero",
    components: {}
};
</script>

<style scoped>

.hero-wrapper > .container {
    padding: 18rem 0 18rem 0;
}
.round-illustration {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.round-illustration img.is-rounded {
    width: 400px;
    border-radius: 100%;
}

.text-faded {
    color: black;
    opacity: 0.7;
}

@media only screen and (max-width: 600px) {
  .hero-wrapper > .container {
    padding: 15rem 0 15rem 0;
}
}
</style>
