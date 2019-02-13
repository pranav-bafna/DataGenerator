// ORM class for table 'claim_il_temp'
// WARNING: This class is AUTO-GENERATED. Modify at your own risk.
//
// Debug information:
// Generated date: Tue Feb 12 01:16:42 PST 2019
// For connector: org.apache.sqoop.manager.GenericJdbcManager
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapred.lib.db.DBWritable;
import com.cloudera.sqoop.lib.JdbcWritableBridge;
import com.cloudera.sqoop.lib.DelimiterSet;
import com.cloudera.sqoop.lib.FieldFormatter;
import com.cloudera.sqoop.lib.RecordParser;
import com.cloudera.sqoop.lib.BooleanParser;
import com.cloudera.sqoop.lib.BlobRef;
import com.cloudera.sqoop.lib.ClobRef;
import com.cloudera.sqoop.lib.LargeObjectLoader;
import com.cloudera.sqoop.lib.SqoopRecord;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class claim_il_temp extends SqoopRecord  implements DBWritable, Writable {
  private final int PROTOCOL_VERSION = 3;
  public int getClassFormatVersion() { return PROTOCOL_VERSION; }
  public static interface FieldSetterCommand {    void setField(Object value);  }  protected ResultSet __cur_result_set;
  private Map<String, FieldSetterCommand> setters = new HashMap<String, FieldSetterCommand>();
  private void init0() {
    setters.put("claim_id", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_id = (String)value;
      }
    });
    setters.put("claim_claimnumber", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_claimnumber = (String)value;
      }
    });
    setters.put("policy_number", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        policy_number = (String)value;
      }
    });
    setters.put("incident_id", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        incident_id = (String)value;
      }
    });
    setters.put("claim_lossdate", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_lossdate = (java.sql.Timestamp)value;
      }
    });
    setters.put("claim_reporteddate", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_reporteddate = (java.sql.Timestamp)value;
      }
    });
    setters.put("claim_status", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_status = (String)value;
      }
    });
    setters.put("claim_closedate", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_closedate = (java.sql.Timestamp)value;
      }
    });
    setters.put("claim_losstype", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_losstype = (String)value;
      }
    });
    setters.put("claim_lob", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_lob = (String)value;
      }
    });
    setters.put("claim_severity", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_severity = (String)value;
      }
    });
    setters.put("claim_loss_add_state", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_loss_add_state = (String)value;
      }
    });
    setters.put("claim_glass_ind", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_glass_ind = (String)value;
      }
    });
    setters.put("claim_primary_group", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_primary_group = (String)value;
      }
    });
    setters.put("claim_primary_adjuster_id", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_primary_adjuster_id = (String)value;
      }
    });
    setters.put("claim_litigation_ind", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_litigation_ind = (String)value;
      }
    });
    setters.put("claim_subrogation_status", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_subrogation_status = (String)value;
      }
    });
    setters.put("claim_salvage_status", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_salvage_status = (String)value;
      }
    });
    setters.put("claim_litigation_status", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_litigation_status = (String)value;
      }
    });
    setters.put("claim_fatalities", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_fatalities = (String)value;
      }
    });
    setters.put("claim_large_loss", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_large_loss = (String)value;
      }
    });
    setters.put("claim_coverage_in_question", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_coverage_in_question = (String)value;
      }
    });
    setters.put("claim_siu_status", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_siu_status = (String)value;
      }
    });
    setters.put("claim_siu_score", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_siu_score = (String)value;
      }
    });
    setters.put("claim_resolution", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        claim_resolution = (String)value;
      }
    });
  }
  public claim_il_temp() {
    init0();
  }
  private String claim_id;
  public String get_claim_id() {
    return claim_id;
  }
  public void set_claim_id(String claim_id) {
    this.claim_id = claim_id;
  }
  public claim_il_temp with_claim_id(String claim_id) {
    this.claim_id = claim_id;
    return this;
  }
  private String claim_claimnumber;
  public String get_claim_claimnumber() {
    return claim_claimnumber;
  }
  public void set_claim_claimnumber(String claim_claimnumber) {
    this.claim_claimnumber = claim_claimnumber;
  }
  public claim_il_temp with_claim_claimnumber(String claim_claimnumber) {
    this.claim_claimnumber = claim_claimnumber;
    return this;
  }
  private String policy_number;
  public String get_policy_number() {
    return policy_number;
  }
  public void set_policy_number(String policy_number) {
    this.policy_number = policy_number;
  }
  public claim_il_temp with_policy_number(String policy_number) {
    this.policy_number = policy_number;
    return this;
  }
  private String incident_id;
  public String get_incident_id() {
    return incident_id;
  }
  public void set_incident_id(String incident_id) {
    this.incident_id = incident_id;
  }
  public claim_il_temp with_incident_id(String incident_id) {
    this.incident_id = incident_id;
    return this;
  }
  private java.sql.Timestamp claim_lossdate;
  public java.sql.Timestamp get_claim_lossdate() {
    return claim_lossdate;
  }
  public void set_claim_lossdate(java.sql.Timestamp claim_lossdate) {
    this.claim_lossdate = claim_lossdate;
  }
  public claim_il_temp with_claim_lossdate(java.sql.Timestamp claim_lossdate) {
    this.claim_lossdate = claim_lossdate;
    return this;
  }
  private java.sql.Timestamp claim_reporteddate;
  public java.sql.Timestamp get_claim_reporteddate() {
    return claim_reporteddate;
  }
  public void set_claim_reporteddate(java.sql.Timestamp claim_reporteddate) {
    this.claim_reporteddate = claim_reporteddate;
  }
  public claim_il_temp with_claim_reporteddate(java.sql.Timestamp claim_reporteddate) {
    this.claim_reporteddate = claim_reporteddate;
    return this;
  }
  private String claim_status;
  public String get_claim_status() {
    return claim_status;
  }
  public void set_claim_status(String claim_status) {
    this.claim_status = claim_status;
  }
  public claim_il_temp with_claim_status(String claim_status) {
    this.claim_status = claim_status;
    return this;
  }
  private java.sql.Timestamp claim_closedate;
  public java.sql.Timestamp get_claim_closedate() {
    return claim_closedate;
  }
  public void set_claim_closedate(java.sql.Timestamp claim_closedate) {
    this.claim_closedate = claim_closedate;
  }
  public claim_il_temp with_claim_closedate(java.sql.Timestamp claim_closedate) {
    this.claim_closedate = claim_closedate;
    return this;
  }
  private String claim_losstype;
  public String get_claim_losstype() {
    return claim_losstype;
  }
  public void set_claim_losstype(String claim_losstype) {
    this.claim_losstype = claim_losstype;
  }
  public claim_il_temp with_claim_losstype(String claim_losstype) {
    this.claim_losstype = claim_losstype;
    return this;
  }
  private String claim_lob;
  public String get_claim_lob() {
    return claim_lob;
  }
  public void set_claim_lob(String claim_lob) {
    this.claim_lob = claim_lob;
  }
  public claim_il_temp with_claim_lob(String claim_lob) {
    this.claim_lob = claim_lob;
    return this;
  }
  private String claim_severity;
  public String get_claim_severity() {
    return claim_severity;
  }
  public void set_claim_severity(String claim_severity) {
    this.claim_severity = claim_severity;
  }
  public claim_il_temp with_claim_severity(String claim_severity) {
    this.claim_severity = claim_severity;
    return this;
  }
  private String claim_loss_add_state;
  public String get_claim_loss_add_state() {
    return claim_loss_add_state;
  }
  public void set_claim_loss_add_state(String claim_loss_add_state) {
    this.claim_loss_add_state = claim_loss_add_state;
  }
  public claim_il_temp with_claim_loss_add_state(String claim_loss_add_state) {
    this.claim_loss_add_state = claim_loss_add_state;
    return this;
  }
  private String claim_glass_ind;
  public String get_claim_glass_ind() {
    return claim_glass_ind;
  }
  public void set_claim_glass_ind(String claim_glass_ind) {
    this.claim_glass_ind = claim_glass_ind;
  }
  public claim_il_temp with_claim_glass_ind(String claim_glass_ind) {
    this.claim_glass_ind = claim_glass_ind;
    return this;
  }
  private String claim_primary_group;
  public String get_claim_primary_group() {
    return claim_primary_group;
  }
  public void set_claim_primary_group(String claim_primary_group) {
    this.claim_primary_group = claim_primary_group;
  }
  public claim_il_temp with_claim_primary_group(String claim_primary_group) {
    this.claim_primary_group = claim_primary_group;
    return this;
  }
  private String claim_primary_adjuster_id;
  public String get_claim_primary_adjuster_id() {
    return claim_primary_adjuster_id;
  }
  public void set_claim_primary_adjuster_id(String claim_primary_adjuster_id) {
    this.claim_primary_adjuster_id = claim_primary_adjuster_id;
  }
  public claim_il_temp with_claim_primary_adjuster_id(String claim_primary_adjuster_id) {
    this.claim_primary_adjuster_id = claim_primary_adjuster_id;
    return this;
  }
  private String claim_litigation_ind;
  public String get_claim_litigation_ind() {
    return claim_litigation_ind;
  }
  public void set_claim_litigation_ind(String claim_litigation_ind) {
    this.claim_litigation_ind = claim_litigation_ind;
  }
  public claim_il_temp with_claim_litigation_ind(String claim_litigation_ind) {
    this.claim_litigation_ind = claim_litigation_ind;
    return this;
  }
  private String claim_subrogation_status;
  public String get_claim_subrogation_status() {
    return claim_subrogation_status;
  }
  public void set_claim_subrogation_status(String claim_subrogation_status) {
    this.claim_subrogation_status = claim_subrogation_status;
  }
  public claim_il_temp with_claim_subrogation_status(String claim_subrogation_status) {
    this.claim_subrogation_status = claim_subrogation_status;
    return this;
  }
  private String claim_salvage_status;
  public String get_claim_salvage_status() {
    return claim_salvage_status;
  }
  public void set_claim_salvage_status(String claim_salvage_status) {
    this.claim_salvage_status = claim_salvage_status;
  }
  public claim_il_temp with_claim_salvage_status(String claim_salvage_status) {
    this.claim_salvage_status = claim_salvage_status;
    return this;
  }
  private String claim_litigation_status;
  public String get_claim_litigation_status() {
    return claim_litigation_status;
  }
  public void set_claim_litigation_status(String claim_litigation_status) {
    this.claim_litigation_status = claim_litigation_status;
  }
  public claim_il_temp with_claim_litigation_status(String claim_litigation_status) {
    this.claim_litigation_status = claim_litigation_status;
    return this;
  }
  private String claim_fatalities;
  public String get_claim_fatalities() {
    return claim_fatalities;
  }
  public void set_claim_fatalities(String claim_fatalities) {
    this.claim_fatalities = claim_fatalities;
  }
  public claim_il_temp with_claim_fatalities(String claim_fatalities) {
    this.claim_fatalities = claim_fatalities;
    return this;
  }
  private String claim_large_loss;
  public String get_claim_large_loss() {
    return claim_large_loss;
  }
  public void set_claim_large_loss(String claim_large_loss) {
    this.claim_large_loss = claim_large_loss;
  }
  public claim_il_temp with_claim_large_loss(String claim_large_loss) {
    this.claim_large_loss = claim_large_loss;
    return this;
  }
  private String claim_coverage_in_question;
  public String get_claim_coverage_in_question() {
    return claim_coverage_in_question;
  }
  public void set_claim_coverage_in_question(String claim_coverage_in_question) {
    this.claim_coverage_in_question = claim_coverage_in_question;
  }
  public claim_il_temp with_claim_coverage_in_question(String claim_coverage_in_question) {
    this.claim_coverage_in_question = claim_coverage_in_question;
    return this;
  }
  private String claim_siu_status;
  public String get_claim_siu_status() {
    return claim_siu_status;
  }
  public void set_claim_siu_status(String claim_siu_status) {
    this.claim_siu_status = claim_siu_status;
  }
  public claim_il_temp with_claim_siu_status(String claim_siu_status) {
    this.claim_siu_status = claim_siu_status;
    return this;
  }
  private String claim_siu_score;
  public String get_claim_siu_score() {
    return claim_siu_score;
  }
  public void set_claim_siu_score(String claim_siu_score) {
    this.claim_siu_score = claim_siu_score;
  }
  public claim_il_temp with_claim_siu_score(String claim_siu_score) {
    this.claim_siu_score = claim_siu_score;
    return this;
  }
  private String claim_resolution;
  public String get_claim_resolution() {
    return claim_resolution;
  }
  public void set_claim_resolution(String claim_resolution) {
    this.claim_resolution = claim_resolution;
  }
  public claim_il_temp with_claim_resolution(String claim_resolution) {
    this.claim_resolution = claim_resolution;
    return this;
  }
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof claim_il_temp)) {
      return false;
    }
    claim_il_temp that = (claim_il_temp) o;
    boolean equal = true;
    equal = equal && (this.claim_id == null ? that.claim_id == null : this.claim_id.equals(that.claim_id));
    equal = equal && (this.claim_claimnumber == null ? that.claim_claimnumber == null : this.claim_claimnumber.equals(that.claim_claimnumber));
    equal = equal && (this.policy_number == null ? that.policy_number == null : this.policy_number.equals(that.policy_number));
    equal = equal && (this.incident_id == null ? that.incident_id == null : this.incident_id.equals(that.incident_id));
    equal = equal && (this.claim_lossdate == null ? that.claim_lossdate == null : this.claim_lossdate.equals(that.claim_lossdate));
    equal = equal && (this.claim_reporteddate == null ? that.claim_reporteddate == null : this.claim_reporteddate.equals(that.claim_reporteddate));
    equal = equal && (this.claim_status == null ? that.claim_status == null : this.claim_status.equals(that.claim_status));
    equal = equal && (this.claim_closedate == null ? that.claim_closedate == null : this.claim_closedate.equals(that.claim_closedate));
    equal = equal && (this.claim_losstype == null ? that.claim_losstype == null : this.claim_losstype.equals(that.claim_losstype));
    equal = equal && (this.claim_lob == null ? that.claim_lob == null : this.claim_lob.equals(that.claim_lob));
    equal = equal && (this.claim_severity == null ? that.claim_severity == null : this.claim_severity.equals(that.claim_severity));
    equal = equal && (this.claim_loss_add_state == null ? that.claim_loss_add_state == null : this.claim_loss_add_state.equals(that.claim_loss_add_state));
    equal = equal && (this.claim_glass_ind == null ? that.claim_glass_ind == null : this.claim_glass_ind.equals(that.claim_glass_ind));
    equal = equal && (this.claim_primary_group == null ? that.claim_primary_group == null : this.claim_primary_group.equals(that.claim_primary_group));
    equal = equal && (this.claim_primary_adjuster_id == null ? that.claim_primary_adjuster_id == null : this.claim_primary_adjuster_id.equals(that.claim_primary_adjuster_id));
    equal = equal && (this.claim_litigation_ind == null ? that.claim_litigation_ind == null : this.claim_litigation_ind.equals(that.claim_litigation_ind));
    equal = equal && (this.claim_subrogation_status == null ? that.claim_subrogation_status == null : this.claim_subrogation_status.equals(that.claim_subrogation_status));
    equal = equal && (this.claim_salvage_status == null ? that.claim_salvage_status == null : this.claim_salvage_status.equals(that.claim_salvage_status));
    equal = equal && (this.claim_litigation_status == null ? that.claim_litigation_status == null : this.claim_litigation_status.equals(that.claim_litigation_status));
    equal = equal && (this.claim_fatalities == null ? that.claim_fatalities == null : this.claim_fatalities.equals(that.claim_fatalities));
    equal = equal && (this.claim_large_loss == null ? that.claim_large_loss == null : this.claim_large_loss.equals(that.claim_large_loss));
    equal = equal && (this.claim_coverage_in_question == null ? that.claim_coverage_in_question == null : this.claim_coverage_in_question.equals(that.claim_coverage_in_question));
    equal = equal && (this.claim_siu_status == null ? that.claim_siu_status == null : this.claim_siu_status.equals(that.claim_siu_status));
    equal = equal && (this.claim_siu_score == null ? that.claim_siu_score == null : this.claim_siu_score.equals(that.claim_siu_score));
    equal = equal && (this.claim_resolution == null ? that.claim_resolution == null : this.claim_resolution.equals(that.claim_resolution));
    return equal;
  }
  public boolean equals0(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof claim_il_temp)) {
      return false;
    }
    claim_il_temp that = (claim_il_temp) o;
    boolean equal = true;
    equal = equal && (this.claim_id == null ? that.claim_id == null : this.claim_id.equals(that.claim_id));
    equal = equal && (this.claim_claimnumber == null ? that.claim_claimnumber == null : this.claim_claimnumber.equals(that.claim_claimnumber));
    equal = equal && (this.policy_number == null ? that.policy_number == null : this.policy_number.equals(that.policy_number));
    equal = equal && (this.incident_id == null ? that.incident_id == null : this.incident_id.equals(that.incident_id));
    equal = equal && (this.claim_lossdate == null ? that.claim_lossdate == null : this.claim_lossdate.equals(that.claim_lossdate));
    equal = equal && (this.claim_reporteddate == null ? that.claim_reporteddate == null : this.claim_reporteddate.equals(that.claim_reporteddate));
    equal = equal && (this.claim_status == null ? that.claim_status == null : this.claim_status.equals(that.claim_status));
    equal = equal && (this.claim_closedate == null ? that.claim_closedate == null : this.claim_closedate.equals(that.claim_closedate));
    equal = equal && (this.claim_losstype == null ? that.claim_losstype == null : this.claim_losstype.equals(that.claim_losstype));
    equal = equal && (this.claim_lob == null ? that.claim_lob == null : this.claim_lob.equals(that.claim_lob));
    equal = equal && (this.claim_severity == null ? that.claim_severity == null : this.claim_severity.equals(that.claim_severity));
    equal = equal && (this.claim_loss_add_state == null ? that.claim_loss_add_state == null : this.claim_loss_add_state.equals(that.claim_loss_add_state));
    equal = equal && (this.claim_glass_ind == null ? that.claim_glass_ind == null : this.claim_glass_ind.equals(that.claim_glass_ind));
    equal = equal && (this.claim_primary_group == null ? that.claim_primary_group == null : this.claim_primary_group.equals(that.claim_primary_group));
    equal = equal && (this.claim_primary_adjuster_id == null ? that.claim_primary_adjuster_id == null : this.claim_primary_adjuster_id.equals(that.claim_primary_adjuster_id));
    equal = equal && (this.claim_litigation_ind == null ? that.claim_litigation_ind == null : this.claim_litigation_ind.equals(that.claim_litigation_ind));
    equal = equal && (this.claim_subrogation_status == null ? that.claim_subrogation_status == null : this.claim_subrogation_status.equals(that.claim_subrogation_status));
    equal = equal && (this.claim_salvage_status == null ? that.claim_salvage_status == null : this.claim_salvage_status.equals(that.claim_salvage_status));
    equal = equal && (this.claim_litigation_status == null ? that.claim_litigation_status == null : this.claim_litigation_status.equals(that.claim_litigation_status));
    equal = equal && (this.claim_fatalities == null ? that.claim_fatalities == null : this.claim_fatalities.equals(that.claim_fatalities));
    equal = equal && (this.claim_large_loss == null ? that.claim_large_loss == null : this.claim_large_loss.equals(that.claim_large_loss));
    equal = equal && (this.claim_coverage_in_question == null ? that.claim_coverage_in_question == null : this.claim_coverage_in_question.equals(that.claim_coverage_in_question));
    equal = equal && (this.claim_siu_status == null ? that.claim_siu_status == null : this.claim_siu_status.equals(that.claim_siu_status));
    equal = equal && (this.claim_siu_score == null ? that.claim_siu_score == null : this.claim_siu_score.equals(that.claim_siu_score));
    equal = equal && (this.claim_resolution == null ? that.claim_resolution == null : this.claim_resolution.equals(that.claim_resolution));
    return equal;
  }
  public void readFields(ResultSet __dbResults) throws SQLException {
    this.__cur_result_set = __dbResults;
    this.claim_id = JdbcWritableBridge.readString(1, __dbResults);
    this.claim_claimnumber = JdbcWritableBridge.readString(2, __dbResults);
    this.policy_number = JdbcWritableBridge.readString(3, __dbResults);
    this.incident_id = JdbcWritableBridge.readString(4, __dbResults);
    this.claim_lossdate = JdbcWritableBridge.readTimestamp(5, __dbResults);
    this.claim_reporteddate = JdbcWritableBridge.readTimestamp(6, __dbResults);
    this.claim_status = JdbcWritableBridge.readString(7, __dbResults);
    this.claim_closedate = JdbcWritableBridge.readTimestamp(8, __dbResults);
    this.claim_losstype = JdbcWritableBridge.readString(9, __dbResults);
    this.claim_lob = JdbcWritableBridge.readString(10, __dbResults);
    this.claim_severity = JdbcWritableBridge.readString(11, __dbResults);
    this.claim_loss_add_state = JdbcWritableBridge.readString(12, __dbResults);
    this.claim_glass_ind = JdbcWritableBridge.readString(13, __dbResults);
    this.claim_primary_group = JdbcWritableBridge.readString(14, __dbResults);
    this.claim_primary_adjuster_id = JdbcWritableBridge.readString(15, __dbResults);
    this.claim_litigation_ind = JdbcWritableBridge.readString(16, __dbResults);
    this.claim_subrogation_status = JdbcWritableBridge.readString(17, __dbResults);
    this.claim_salvage_status = JdbcWritableBridge.readString(18, __dbResults);
    this.claim_litigation_status = JdbcWritableBridge.readString(19, __dbResults);
    this.claim_fatalities = JdbcWritableBridge.readString(20, __dbResults);
    this.claim_large_loss = JdbcWritableBridge.readString(21, __dbResults);
    this.claim_coverage_in_question = JdbcWritableBridge.readString(22, __dbResults);
    this.claim_siu_status = JdbcWritableBridge.readString(23, __dbResults);
    this.claim_siu_score = JdbcWritableBridge.readString(24, __dbResults);
    this.claim_resolution = JdbcWritableBridge.readString(25, __dbResults);
  }
  public void readFields0(ResultSet __dbResults) throws SQLException {
    this.claim_id = JdbcWritableBridge.readString(1, __dbResults);
    this.claim_claimnumber = JdbcWritableBridge.readString(2, __dbResults);
    this.policy_number = JdbcWritableBridge.readString(3, __dbResults);
    this.incident_id = JdbcWritableBridge.readString(4, __dbResults);
    this.claim_lossdate = JdbcWritableBridge.readTimestamp(5, __dbResults);
    this.claim_reporteddate = JdbcWritableBridge.readTimestamp(6, __dbResults);
    this.claim_status = JdbcWritableBridge.readString(7, __dbResults);
    this.claim_closedate = JdbcWritableBridge.readTimestamp(8, __dbResults);
    this.claim_losstype = JdbcWritableBridge.readString(9, __dbResults);
    this.claim_lob = JdbcWritableBridge.readString(10, __dbResults);
    this.claim_severity = JdbcWritableBridge.readString(11, __dbResults);
    this.claim_loss_add_state = JdbcWritableBridge.readString(12, __dbResults);
    this.claim_glass_ind = JdbcWritableBridge.readString(13, __dbResults);
    this.claim_primary_group = JdbcWritableBridge.readString(14, __dbResults);
    this.claim_primary_adjuster_id = JdbcWritableBridge.readString(15, __dbResults);
    this.claim_litigation_ind = JdbcWritableBridge.readString(16, __dbResults);
    this.claim_subrogation_status = JdbcWritableBridge.readString(17, __dbResults);
    this.claim_salvage_status = JdbcWritableBridge.readString(18, __dbResults);
    this.claim_litigation_status = JdbcWritableBridge.readString(19, __dbResults);
    this.claim_fatalities = JdbcWritableBridge.readString(20, __dbResults);
    this.claim_large_loss = JdbcWritableBridge.readString(21, __dbResults);
    this.claim_coverage_in_question = JdbcWritableBridge.readString(22, __dbResults);
    this.claim_siu_status = JdbcWritableBridge.readString(23, __dbResults);
    this.claim_siu_score = JdbcWritableBridge.readString(24, __dbResults);
    this.claim_resolution = JdbcWritableBridge.readString(25, __dbResults);
  }
  public void loadLargeObjects(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void loadLargeObjects0(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void write(PreparedStatement __dbStmt) throws SQLException {
    write(__dbStmt, 0);
  }

  public int write(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeString(claim_id, 1 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_claimnumber, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(policy_number, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(incident_id, 4 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeTimestamp(claim_lossdate, 5 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeTimestamp(claim_reporteddate, 6 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeString(claim_status, 7 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeTimestamp(claim_closedate, 8 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeString(claim_losstype, 9 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_lob, 10 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_severity, 11 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_loss_add_state, 12 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_glass_ind, 13 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_primary_group, 14 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_primary_adjuster_id, 15 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_litigation_ind, 16 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_subrogation_status, 17 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_salvage_status, 18 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_litigation_status, 19 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_fatalities, 20 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_large_loss, 21 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_coverage_in_question, 22 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_siu_status, 23 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_siu_score, 24 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_resolution, 25 + __off, 12, __dbStmt);
    return 25;
  }
  public void write0(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeString(claim_id, 1 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_claimnumber, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(policy_number, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(incident_id, 4 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeTimestamp(claim_lossdate, 5 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeTimestamp(claim_reporteddate, 6 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeString(claim_status, 7 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeTimestamp(claim_closedate, 8 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeString(claim_losstype, 9 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_lob, 10 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_severity, 11 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_loss_add_state, 12 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_glass_ind, 13 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_primary_group, 14 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_primary_adjuster_id, 15 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_litigation_ind, 16 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_subrogation_status, 17 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_salvage_status, 18 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_litigation_status, 19 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_fatalities, 20 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_large_loss, 21 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_coverage_in_question, 22 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_siu_status, 23 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_siu_score, 24 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(claim_resolution, 25 + __off, 12, __dbStmt);
  }
  public void readFields(DataInput __dataIn) throws IOException {
this.readFields0(__dataIn);  }
  public void readFields0(DataInput __dataIn) throws IOException {
    if (__dataIn.readBoolean()) { 
        this.claim_id = null;
    } else {
    this.claim_id = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_claimnumber = null;
    } else {
    this.claim_claimnumber = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.policy_number = null;
    } else {
    this.policy_number = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.incident_id = null;
    } else {
    this.incident_id = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_lossdate = null;
    } else {
    this.claim_lossdate = new Timestamp(__dataIn.readLong());
    this.claim_lossdate.setNanos(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.claim_reporteddate = null;
    } else {
    this.claim_reporteddate = new Timestamp(__dataIn.readLong());
    this.claim_reporteddate.setNanos(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.claim_status = null;
    } else {
    this.claim_status = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_closedate = null;
    } else {
    this.claim_closedate = new Timestamp(__dataIn.readLong());
    this.claim_closedate.setNanos(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.claim_losstype = null;
    } else {
    this.claim_losstype = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_lob = null;
    } else {
    this.claim_lob = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_severity = null;
    } else {
    this.claim_severity = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_loss_add_state = null;
    } else {
    this.claim_loss_add_state = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_glass_ind = null;
    } else {
    this.claim_glass_ind = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_primary_group = null;
    } else {
    this.claim_primary_group = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_primary_adjuster_id = null;
    } else {
    this.claim_primary_adjuster_id = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_litigation_ind = null;
    } else {
    this.claim_litigation_ind = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_subrogation_status = null;
    } else {
    this.claim_subrogation_status = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_salvage_status = null;
    } else {
    this.claim_salvage_status = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_litigation_status = null;
    } else {
    this.claim_litigation_status = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_fatalities = null;
    } else {
    this.claim_fatalities = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_large_loss = null;
    } else {
    this.claim_large_loss = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_coverage_in_question = null;
    } else {
    this.claim_coverage_in_question = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_siu_status = null;
    } else {
    this.claim_siu_status = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_siu_score = null;
    } else {
    this.claim_siu_score = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.claim_resolution = null;
    } else {
    this.claim_resolution = Text.readString(__dataIn);
    }
  }
  public void write(DataOutput __dataOut) throws IOException {
    if (null == this.claim_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_id);
    }
    if (null == this.claim_claimnumber) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_claimnumber);
    }
    if (null == this.policy_number) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, policy_number);
    }
    if (null == this.incident_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, incident_id);
    }
    if (null == this.claim_lossdate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.claim_lossdate.getTime());
    __dataOut.writeInt(this.claim_lossdate.getNanos());
    }
    if (null == this.claim_reporteddate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.claim_reporteddate.getTime());
    __dataOut.writeInt(this.claim_reporteddate.getNanos());
    }
    if (null == this.claim_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_status);
    }
    if (null == this.claim_closedate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.claim_closedate.getTime());
    __dataOut.writeInt(this.claim_closedate.getNanos());
    }
    if (null == this.claim_losstype) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_losstype);
    }
    if (null == this.claim_lob) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_lob);
    }
    if (null == this.claim_severity) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_severity);
    }
    if (null == this.claim_loss_add_state) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_loss_add_state);
    }
    if (null == this.claim_glass_ind) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_glass_ind);
    }
    if (null == this.claim_primary_group) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_primary_group);
    }
    if (null == this.claim_primary_adjuster_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_primary_adjuster_id);
    }
    if (null == this.claim_litigation_ind) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_litigation_ind);
    }
    if (null == this.claim_subrogation_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_subrogation_status);
    }
    if (null == this.claim_salvage_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_salvage_status);
    }
    if (null == this.claim_litigation_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_litigation_status);
    }
    if (null == this.claim_fatalities) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_fatalities);
    }
    if (null == this.claim_large_loss) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_large_loss);
    }
    if (null == this.claim_coverage_in_question) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_coverage_in_question);
    }
    if (null == this.claim_siu_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_siu_status);
    }
    if (null == this.claim_siu_score) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_siu_score);
    }
    if (null == this.claim_resolution) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_resolution);
    }
  }
  public void write0(DataOutput __dataOut) throws IOException {
    if (null == this.claim_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_id);
    }
    if (null == this.claim_claimnumber) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_claimnumber);
    }
    if (null == this.policy_number) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, policy_number);
    }
    if (null == this.incident_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, incident_id);
    }
    if (null == this.claim_lossdate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.claim_lossdate.getTime());
    __dataOut.writeInt(this.claim_lossdate.getNanos());
    }
    if (null == this.claim_reporteddate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.claim_reporteddate.getTime());
    __dataOut.writeInt(this.claim_reporteddate.getNanos());
    }
    if (null == this.claim_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_status);
    }
    if (null == this.claim_closedate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.claim_closedate.getTime());
    __dataOut.writeInt(this.claim_closedate.getNanos());
    }
    if (null == this.claim_losstype) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_losstype);
    }
    if (null == this.claim_lob) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_lob);
    }
    if (null == this.claim_severity) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_severity);
    }
    if (null == this.claim_loss_add_state) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_loss_add_state);
    }
    if (null == this.claim_glass_ind) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_glass_ind);
    }
    if (null == this.claim_primary_group) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_primary_group);
    }
    if (null == this.claim_primary_adjuster_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_primary_adjuster_id);
    }
    if (null == this.claim_litigation_ind) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_litigation_ind);
    }
    if (null == this.claim_subrogation_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_subrogation_status);
    }
    if (null == this.claim_salvage_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_salvage_status);
    }
    if (null == this.claim_litigation_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_litigation_status);
    }
    if (null == this.claim_fatalities) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_fatalities);
    }
    if (null == this.claim_large_loss) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_large_loss);
    }
    if (null == this.claim_coverage_in_question) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_coverage_in_question);
    }
    if (null == this.claim_siu_status) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_siu_status);
    }
    if (null == this.claim_siu_score) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_siu_score);
    }
    if (null == this.claim_resolution) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, claim_resolution);
    }
  }
  private static final DelimiterSet __outputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  public String toString() {
    return toString(__outputDelimiters, true);
  }
  public String toString(DelimiterSet delimiters) {
    return toString(delimiters, true);
  }
  public String toString(boolean useRecordDelim) {
    return toString(__outputDelimiters, useRecordDelim);
  }
  public String toString(DelimiterSet delimiters, boolean useRecordDelim) {
    StringBuilder __sb = new StringBuilder();
    char fieldDelim = delimiters.getFieldsTerminatedBy();
    __sb.append(FieldFormatter.escapeAndEnclose(claim_id==null?"null":claim_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_claimnumber==null?"null":claim_claimnumber, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(policy_number==null?"null":policy_number, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(incident_id==null?"null":incident_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_lossdate==null?"null":"" + claim_lossdate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_reporteddate==null?"null":"" + claim_reporteddate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_status==null?"null":claim_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_closedate==null?"null":"" + claim_closedate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_losstype==null?"null":claim_losstype, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_lob==null?"null":claim_lob, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_severity==null?"null":claim_severity, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_loss_add_state==null?"null":claim_loss_add_state, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_glass_ind==null?"null":claim_glass_ind, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_primary_group==null?"null":claim_primary_group, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_primary_adjuster_id==null?"null":claim_primary_adjuster_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_litigation_ind==null?"null":claim_litigation_ind, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_subrogation_status==null?"null":claim_subrogation_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_salvage_status==null?"null":claim_salvage_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_litigation_status==null?"null":claim_litigation_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_fatalities==null?"null":claim_fatalities, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_large_loss==null?"null":claim_large_loss, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_coverage_in_question==null?"null":claim_coverage_in_question, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_siu_status==null?"null":claim_siu_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_siu_score==null?"null":claim_siu_score, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_resolution==null?"null":claim_resolution, delimiters));
    if (useRecordDelim) {
      __sb.append(delimiters.getLinesTerminatedBy());
    }
    return __sb.toString();
  }
  public void toString0(DelimiterSet delimiters, StringBuilder __sb, char fieldDelim) {
    __sb.append(FieldFormatter.escapeAndEnclose(claim_id==null?"null":claim_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_claimnumber==null?"null":claim_claimnumber, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(policy_number==null?"null":policy_number, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(incident_id==null?"null":incident_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_lossdate==null?"null":"" + claim_lossdate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_reporteddate==null?"null":"" + claim_reporteddate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_status==null?"null":claim_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_closedate==null?"null":"" + claim_closedate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_losstype==null?"null":claim_losstype, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_lob==null?"null":claim_lob, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_severity==null?"null":claim_severity, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_loss_add_state==null?"null":claim_loss_add_state, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_glass_ind==null?"null":claim_glass_ind, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_primary_group==null?"null":claim_primary_group, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_primary_adjuster_id==null?"null":claim_primary_adjuster_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_litigation_ind==null?"null":claim_litigation_ind, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_subrogation_status==null?"null":claim_subrogation_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_salvage_status==null?"null":claim_salvage_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_litigation_status==null?"null":claim_litigation_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_fatalities==null?"null":claim_fatalities, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_large_loss==null?"null":claim_large_loss, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_coverage_in_question==null?"null":claim_coverage_in_question, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_siu_status==null?"null":claim_siu_status, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_siu_score==null?"null":claim_siu_score, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(claim_resolution==null?"null":claim_resolution, delimiters));
  }
  private static final DelimiterSet __inputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  private RecordParser __parser;
  public void parse(Text __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharSequence __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(byte [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(char [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(ByteBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  private void __loadFromFields(List<String> fields) {
    Iterator<String> __it = fields.listIterator();
    String __cur_str = null;
    try {
    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_id = null; } else {
      this.claim_id = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_claimnumber = null; } else {
      this.claim_claimnumber = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.policy_number = null; } else {
      this.policy_number = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.incident_id = null; } else {
      this.incident_id = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.claim_lossdate = null; } else {
      this.claim_lossdate = java.sql.Timestamp.valueOf(__cur_str);
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.claim_reporteddate = null; } else {
      this.claim_reporteddate = java.sql.Timestamp.valueOf(__cur_str);
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_status = null; } else {
      this.claim_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.claim_closedate = null; } else {
      this.claim_closedate = java.sql.Timestamp.valueOf(__cur_str);
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_losstype = null; } else {
      this.claim_losstype = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_lob = null; } else {
      this.claim_lob = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_severity = null; } else {
      this.claim_severity = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_loss_add_state = null; } else {
      this.claim_loss_add_state = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_glass_ind = null; } else {
      this.claim_glass_ind = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_primary_group = null; } else {
      this.claim_primary_group = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_primary_adjuster_id = null; } else {
      this.claim_primary_adjuster_id = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_litigation_ind = null; } else {
      this.claim_litigation_ind = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_subrogation_status = null; } else {
      this.claim_subrogation_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_salvage_status = null; } else {
      this.claim_salvage_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_litigation_status = null; } else {
      this.claim_litigation_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_fatalities = null; } else {
      this.claim_fatalities = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_large_loss = null; } else {
      this.claim_large_loss = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_coverage_in_question = null; } else {
      this.claim_coverage_in_question = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_siu_status = null; } else {
      this.claim_siu_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_siu_score = null; } else {
      this.claim_siu_score = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_resolution = null; } else {
      this.claim_resolution = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  private void __loadFromFields0(Iterator<String> __it) {
    String __cur_str = null;
    try {
    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_id = null; } else {
      this.claim_id = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_claimnumber = null; } else {
      this.claim_claimnumber = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.policy_number = null; } else {
      this.policy_number = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.incident_id = null; } else {
      this.incident_id = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.claim_lossdate = null; } else {
      this.claim_lossdate = java.sql.Timestamp.valueOf(__cur_str);
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.claim_reporteddate = null; } else {
      this.claim_reporteddate = java.sql.Timestamp.valueOf(__cur_str);
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_status = null; } else {
      this.claim_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.claim_closedate = null; } else {
      this.claim_closedate = java.sql.Timestamp.valueOf(__cur_str);
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_losstype = null; } else {
      this.claim_losstype = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_lob = null; } else {
      this.claim_lob = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_severity = null; } else {
      this.claim_severity = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_loss_add_state = null; } else {
      this.claim_loss_add_state = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_glass_ind = null; } else {
      this.claim_glass_ind = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_primary_group = null; } else {
      this.claim_primary_group = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_primary_adjuster_id = null; } else {
      this.claim_primary_adjuster_id = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_litigation_ind = null; } else {
      this.claim_litigation_ind = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_subrogation_status = null; } else {
      this.claim_subrogation_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_salvage_status = null; } else {
      this.claim_salvage_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_litigation_status = null; } else {
      this.claim_litigation_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_fatalities = null; } else {
      this.claim_fatalities = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_large_loss = null; } else {
      this.claim_large_loss = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_coverage_in_question = null; } else {
      this.claim_coverage_in_question = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_siu_status = null; } else {
      this.claim_siu_status = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_siu_score = null; } else {
      this.claim_siu_score = __cur_str;
    }

    __cur_str = __it.next();
    if (__cur_str.equals("null")) { this.claim_resolution = null; } else {
      this.claim_resolution = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  public Object clone() throws CloneNotSupportedException {
    claim_il_temp o = (claim_il_temp) super.clone();
    o.claim_lossdate = (o.claim_lossdate != null) ? (java.sql.Timestamp) o.claim_lossdate.clone() : null;
    o.claim_reporteddate = (o.claim_reporteddate != null) ? (java.sql.Timestamp) o.claim_reporteddate.clone() : null;
    o.claim_closedate = (o.claim_closedate != null) ? (java.sql.Timestamp) o.claim_closedate.clone() : null;
    return o;
  }

  public void clone0(claim_il_temp o) throws CloneNotSupportedException {
    o.claim_lossdate = (o.claim_lossdate != null) ? (java.sql.Timestamp) o.claim_lossdate.clone() : null;
    o.claim_reporteddate = (o.claim_reporteddate != null) ? (java.sql.Timestamp) o.claim_reporteddate.clone() : null;
    o.claim_closedate = (o.claim_closedate != null) ? (java.sql.Timestamp) o.claim_closedate.clone() : null;
  }

  public Map<String, Object> getFieldMap() {
    Map<String, Object> __sqoop$field_map = new HashMap<String, Object>();
    __sqoop$field_map.put("claim_id", this.claim_id);
    __sqoop$field_map.put("claim_claimnumber", this.claim_claimnumber);
    __sqoop$field_map.put("policy_number", this.policy_number);
    __sqoop$field_map.put("incident_id", this.incident_id);
    __sqoop$field_map.put("claim_lossdate", this.claim_lossdate);
    __sqoop$field_map.put("claim_reporteddate", this.claim_reporteddate);
    __sqoop$field_map.put("claim_status", this.claim_status);
    __sqoop$field_map.put("claim_closedate", this.claim_closedate);
    __sqoop$field_map.put("claim_losstype", this.claim_losstype);
    __sqoop$field_map.put("claim_lob", this.claim_lob);
    __sqoop$field_map.put("claim_severity", this.claim_severity);
    __sqoop$field_map.put("claim_loss_add_state", this.claim_loss_add_state);
    __sqoop$field_map.put("claim_glass_ind", this.claim_glass_ind);
    __sqoop$field_map.put("claim_primary_group", this.claim_primary_group);
    __sqoop$field_map.put("claim_primary_adjuster_id", this.claim_primary_adjuster_id);
    __sqoop$field_map.put("claim_litigation_ind", this.claim_litigation_ind);
    __sqoop$field_map.put("claim_subrogation_status", this.claim_subrogation_status);
    __sqoop$field_map.put("claim_salvage_status", this.claim_salvage_status);
    __sqoop$field_map.put("claim_litigation_status", this.claim_litigation_status);
    __sqoop$field_map.put("claim_fatalities", this.claim_fatalities);
    __sqoop$field_map.put("claim_large_loss", this.claim_large_loss);
    __sqoop$field_map.put("claim_coverage_in_question", this.claim_coverage_in_question);
    __sqoop$field_map.put("claim_siu_status", this.claim_siu_status);
    __sqoop$field_map.put("claim_siu_score", this.claim_siu_score);
    __sqoop$field_map.put("claim_resolution", this.claim_resolution);
    return __sqoop$field_map;
  }

  public void getFieldMap0(Map<String, Object> __sqoop$field_map) {
    __sqoop$field_map.put("claim_id", this.claim_id);
    __sqoop$field_map.put("claim_claimnumber", this.claim_claimnumber);
    __sqoop$field_map.put("policy_number", this.policy_number);
    __sqoop$field_map.put("incident_id", this.incident_id);
    __sqoop$field_map.put("claim_lossdate", this.claim_lossdate);
    __sqoop$field_map.put("claim_reporteddate", this.claim_reporteddate);
    __sqoop$field_map.put("claim_status", this.claim_status);
    __sqoop$field_map.put("claim_closedate", this.claim_closedate);
    __sqoop$field_map.put("claim_losstype", this.claim_losstype);
    __sqoop$field_map.put("claim_lob", this.claim_lob);
    __sqoop$field_map.put("claim_severity", this.claim_severity);
    __sqoop$field_map.put("claim_loss_add_state", this.claim_loss_add_state);
    __sqoop$field_map.put("claim_glass_ind", this.claim_glass_ind);
    __sqoop$field_map.put("claim_primary_group", this.claim_primary_group);
    __sqoop$field_map.put("claim_primary_adjuster_id", this.claim_primary_adjuster_id);
    __sqoop$field_map.put("claim_litigation_ind", this.claim_litigation_ind);
    __sqoop$field_map.put("claim_subrogation_status", this.claim_subrogation_status);
    __sqoop$field_map.put("claim_salvage_status", this.claim_salvage_status);
    __sqoop$field_map.put("claim_litigation_status", this.claim_litigation_status);
    __sqoop$field_map.put("claim_fatalities", this.claim_fatalities);
    __sqoop$field_map.put("claim_large_loss", this.claim_large_loss);
    __sqoop$field_map.put("claim_coverage_in_question", this.claim_coverage_in_question);
    __sqoop$field_map.put("claim_siu_status", this.claim_siu_status);
    __sqoop$field_map.put("claim_siu_score", this.claim_siu_score);
    __sqoop$field_map.put("claim_resolution", this.claim_resolution);
  }

  public void setField(String __fieldName, Object __fieldVal) {
    if (!setters.containsKey(__fieldName)) {
      throw new RuntimeException("No such field:"+__fieldName);
    }
    setters.get(__fieldName).setField(__fieldVal);
  }

}
