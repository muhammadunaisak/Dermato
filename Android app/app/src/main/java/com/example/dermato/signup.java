package com.example.dermato;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class signup extends AppCompatActivity {
EditText e1,e2,e3,e4,e5,e6,e7,e8,e9,e10;
RadioButton r1,r2,r3;
Button b1;
SharedPreferences sh;
String fname,lname,gender,place,post,pin,email,phone,age,username,password;
String url;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
        e1=findViewById(R.id.editTextTextPersonName5);
        e2=findViewById(R.id.editTextTextPersonName6);
        e3=findViewById(R.id.editTextTextPersonName7);
        e4=findViewById(R.id.editTextTextPersonName8);
        e5=findViewById(R.id.editTextTextPersonName9);
        e6=findViewById(R.id.editTextTextEmailAddress);
        e7=findViewById(R.id.editTextTextPersonName13);
        e8=findViewById(R.id.editTextTextPersonName14);
        e9=findViewById(R.id.editTextTextPersonName15);
        e10=findViewById(R.id.editTextTextPassword);


        r1=findViewById(R.id.radioButton);
        r2=findViewById(R.id.radioButton2);
        r3=findViewById(R.id.radioButton3);
        b1=findViewById(R.id.button2);



        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                        fname=e1.getText().toString();
                        lname=e2.getText().toString();
                        place=e3.getText().toString();
                        post=e4.getText().toString();
                        pin=e5.getText().toString();
                        email=e6.getText().toString();
                        phone=e7.getText().toString();
                        age=e8.getText().toString();
                        username=e9.getText().toString();
                        password=e10.getText().toString();
                        if(r1.isChecked()){
                            gender=r1.getText().toString();
                        }
                        else if(r2.isChecked()) {
                            gender=r2.getText().toString();
                        }
                        else {
                            gender = r3.getText().toString();
                        }

                if (fname.equalsIgnoreCase("")) {
                    e1.setError("Enter first Name");
                } else if (!fname.matches("^[a-z,A-Z]*$")) {
                    e1.setError("Characters Allowed");
                    e1.requestFocus();
                } else if (lname.equalsIgnoreCase("")) {
                    e2.setError("Enter Second Name");
                } else if (!lname.matches("^[a-z,A-Z]*$")) {
                    e2.setError("Characters Allowed");
                    e2.requestFocus();
                } else if (place.equalsIgnoreCase("")) {
                    e3.setError("Enter Place");
                } else if (!place.matches("^[a-z,A-Z]*$")) {
                    e3.setError("Characters Allowed");
                    e3.requestFocus();
                } else if (post.equalsIgnoreCase("")) {
                    e4.setError("Enter Post");
                } else if (!post.matches("^[a-z,A-Z]*$")) {
                    e4.setError("Characters Allowed");
                    e4.requestFocus();
                } else if (pin.equalsIgnoreCase("")) {
                    e5.setError("Enter Pin");
                } else if (pin.length() != 6) {
                    e5.setError(" Minimum 6 No.s required");
                    e5.requestFocus();
                } else if (email.equalsIgnoreCase("")) {
                    e6.setError("Enter E-mail");
                } else if (!Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
                    e6.setError("Enter Valid E-mail");
                    e6.requestFocus();
                } else if (phone.equalsIgnoreCase("")) {
                    e7.setError("Enter Phone Number");
                } else if (phone.length() != 10) {
                    e7.setError("Minimum 10 No.s Required");
                    e7.requestFocus();
                } else if (age.equalsIgnoreCase("")) {
                    e8.setError("Enter Pin");
                } else if (age.length() != 2) {
                    e8.setError(" age required");
                    e8.requestFocus();
                } else if (username.equalsIgnoreCase("")) {
                    e9.setError("Enter Username");
                } else if (!username.matches("^[a-z,A-Z]*$")) {
                    e9.setError("Characters Allowed");
                    e9.requestFocus();
                } else if (password.equalsIgnoreCase("")) {
                    e10.setError("Enter Password");
                }
                else {

                    RequestQueue queue = Volley.newRequestQueue(signup.this);
                    url = "http://" + sh.getString("ip", "") + ":5000/signup";

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.
                            Log.d("+++++++++++++++++", response);
                            try {
                                JSONObject json = new JSONObject(response);
                                String res = json.getString("task");

                                if (res.equalsIgnoreCase("success")) {
                                    Toast.makeText(signup.this, "Registration success", Toast.LENGTH_SHORT).show();

                                    Intent ik = new Intent(getApplicationContext(), MainActivity2login.class);
                                    startActivity(ik);

                                } else {

                                    Toast.makeText(signup.this, "Invalid", Toast.LENGTH_SHORT).show();

                                }
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }


                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {


                            Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                        }
                    }) {
                        @Override
                        protected Map<String, String> getParams() {
                            Map<String, String> params = new HashMap<String, String>();
                            params.put("firstname", fname);
                            params.put("lastname", lname);
                            params.put("place", place);
                            params.put("post", post);
                            params.put("pin", pin);
                            params.put("email", email);
                            params.put("phone", phone);
                            params.put("age", age);
                            params.put("username", username);
                            params.put("password", password);
                            params.put("gender", gender);

                            return params;
                        }
                    };
                    queue.add(stringRequest);
                }

            }
        });
    }
}