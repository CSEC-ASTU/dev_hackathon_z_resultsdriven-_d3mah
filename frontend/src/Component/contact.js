export const Contact = () => {
  return (
    <div id="contact" class="section db">
      <div class="container">
        <div class="section-title text-left">
          <h3>Contact</h3>
          <p>
            Quisque eget nisl id nulla sagittis auctor quis id. Aliquam quis
            vehicula enim, non aliquam risus.
          </p>
        </div>
        comp
        <div class="row">
          <div class="col-md-12">
            <div class="contact_form">
              <div id="message"></div>
              <form id="contactForm" name="sentMessage" novalidate="novalidate">
                <div class="row">
                  <div class="col-md-6">
                    <div class="form-group">
                      <input
                        class="form-control"
                        id="name"
                        type="text"
                        placeholder="Your Name"
                        required="required"
                        data-validation-required-message="Please enter your name."
                      />
                      <p class="help-block text-danger"></p>
                    </div>
                    <div class="form-group">
                      <input
                        class="form-control"
                        id="email"
                        type="email"
                        placeholder="Your Email"
                        required="required"
                        data-validation-required-message="Please enter your email address."
                      />
                      <p class="help-block text-danger"></p>
                    </div>
                    <div class="form-group">
                      <input
                        class="form-control"
                        id="phone"
                        type="tel"
                        placeholder="Your Phone"
                        required="required"
                        data-validation-required-message="Please enter your phone number."
                      />
                      <p class="help-block text-danger"></p>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <textarea
                        class="form-control"
                        id="message"
                        placeholder="Your Message"
                        required="required"
                        data-validation-required-message="Please enter a message."
                      ></textarea>
                      <p class="help-block text-danger"></p>
                    </div>
                  </div>
                  <div class="clearfix"></div>
                  <div class="col-lg-12 text-center">
                    <div id="success"></div>
                    <button
                      id="sendMessageButton"
                      class="sim-btn btn-hover-new"
                      data-text="Send Message"
                      type="submit"
                    >
                      Send Message
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
