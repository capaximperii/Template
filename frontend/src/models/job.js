class Job {
  constructor() {
    this.job_title = null;
    this.submit_type = "hddsn";
    this.treatment_name = null;
    this.control_name = null;
    this.use_control_list = false;
    this.status = "QUEUED";
    this.analytics_level = 3;
    this.product = null;
    this.target_data = null;
    this.match_key_p_mode = "Auto";

    this.user = null;
    this.user_id = 0;
    this.duration = 0;
  }
}

export default Job;
