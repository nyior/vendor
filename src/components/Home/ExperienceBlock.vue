<template>
    <div class="container">
        <h1 class="container-header text-center">Easy as 1, 2</h1>

        <div class="step step-1">
            <div class="row px-5 justify-content-md-center">
                <div class="col-md">
                    <h2 class="md-3 sub-heading">
                        Create a new  account or login to an existing account
                    </h2>
                    <h3 class="text-muted mt-3">
                        We use this data to grant you permission to functionalities 
                        that are available to logged in users only
                    </h3>
                </div>

                <div class="col-md col-center image mt-md-0 mt-3">
                    <img
                        class="illustration "
                        src="../../assets/svg/undraw_home_screen_4n7s.svg"
                        alt=""
                    />
                </div>
            </div>
        </div>

        <div class="step step-2">
            <div class="row px-5 justify-content-md-center">
                <div class="col-md col-center">
                    <img
                        class="illustration"
                        src="../../assets/svg/undraw_data_xmfy.svg"
                        alt=""
                    />
                </div>
                <div class="col-md mt-md-0 mt-3">
                    <h2 class="md-3 sub-heading">
                        upload ads or search for a product/service
                    </h2>
                    <h3 class="text-muted">
                        immediately start selling on our platform by creating ads or search and discover services/products you seek.
                    </h3>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "ExperienceBlock"
};
</script>
<style scoped>
.container-header {
    font-size: 4rem;
    position: relative;
}
.container {
    padding: 40px 0 40px 0;
}
.step {
    padding: 50px 0 50px 0;
    width: 100%;
}

p{
    font-size: 1.6rem;
}
.step .illustration {
    width: 300px;
}
.step + .step {
    margin: 40px 0 40px 0;
}
.col-center {
    display: flex;
    justify-content: center;
}

@media only screen and (max-width: 600px) {
  
}
</style>
