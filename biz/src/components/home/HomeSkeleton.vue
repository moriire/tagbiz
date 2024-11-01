<script setup>
</script>
<template>
    <slot name="categories"></slot>
    <div class="trusted-section mt-5 overflow-hidden">
        <div class="trusted-section-inner">
            <div class="container">
                <div class="row justify-content-center trusted-row">
                    <div class="col-lg-4 col-md-6 col-12">
                <div class="trusted-badge bg-4 rounded">
                  <div class="trusted-icon">
                    <img class="icon-trusted" src="/src/assets/img/trusted/4.png" alt="icon-1">
                  </div>
                  <div class="trusted-content">
                    <h2 class="heading_18 trusted-heading text-white">Pickup & Delivery Option</h2>
                    <p class="text_16 trusted-subheading trusted-subheading-3">Free Pickup & Delivery Option</p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 col-12">
                <div class="trusted-badge bg-4 rounded">
                  <div class="trusted-icon">
                    <img class="icon-trusted" src="/src/assets/img/trusted/5.png" alt="icon-2">
                  </div>
                  <div class="trusted-content">
                    <h2 class="heading_18 trusted-heading text-white">Customer Support 24/7</h2>
                    <p class="text_16 trusted-subheading trusted-subheading-3">Instant access to support</p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 col-12">
                <div class="trusted-badge bg-4 rounded">
                  <div class="trusted-icon">
                    <img class="icon-trusted" src="/src/assets/img/trusted/6.png" alt="icon-3">
                  </div>
                  <div class="trusted-content">
                    <h2 class="heading_18 trusted-heading text-white">100% Secure Payment</h2>
                    <p class="text_16 trusted-subheading trusted-subheading-3">We ensure secure payment!</p>
                  </div>
                </div>
              </div>
                </div>
            </div>
        </div>
    </div>
    <slot name="latest"></slot>
    <!--slot name="discounted"></slot>
    <slot name="popular"></slot-->
</template>