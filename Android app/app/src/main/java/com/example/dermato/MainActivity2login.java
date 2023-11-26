package com.example.dermato;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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

public class MainActivity2login extends AppCompatActivity {
    EditText e1,e2;
    Button b1,b2;
    SharedPreferences sh;
    String username,password,url;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_activity2login);
        e1=findViewById(R.id.editTextTextPersonName2);
        e2=findViewById(R.id.editTextTextPersonName4);
        b1=findViewById(R.id.button3);
        b2=findViewById(R.id.button4);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                username=e1.getText().toString();

                password=e2.getText().toString();
                if (username.equalsIgnoreCase("")) {
                    e1.setError("Enter username");

                }
                else if (password.equalsIgnoreCase("")) {
                    e2.setError("Enter password");
                }
                else {

                    RequestQueue queue = Volley.newRequestQueue(MainActivity2login.this);
                    url = "http://" + sh.getString("ip", "") + ":5000/login";

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.
                            Log.d("+++++++++++++++++", response);
                            try {
//                                Toast.makeText(MainActivity2login.this, ""+response, Toast.LENGTH_SHORT).show();
                                JSONObject json = new JSONObject(response);
                                String res = json.getString("task");

                                if (res.equalsIgnoreCase("success")) {
                                    String lid = json.getString("lid");
                                    String name = json.getString("fname") + " " + json.getString("lname");
                                    SharedPreferences.Editor edp = sh.edit();
                                    edp.putString("lid", lid);
                                    edp.putString("username", name);
                                    edp.commit();
                                    Intent ik = new Intent(getApplicationContext(), hompg.class);
                                    startActivity(ik);

                                } else {

                                    Toast.makeText(MainActivity2login.this, "Invalid username or password", Toast.LENGTH_SHORT).show();

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
                            params.put("uname", username);
                            params.put("password", password);

                            return params;
                        }
                    };
                    queue.add(stringRequest);
                }



            }
        });
        b2.setOnClickListener(new View.OnClickListener()

            {
                @Override
                public void onClick (View view){
                Intent ii = new Intent(getApplicationContext(), signup.class);
                startActivity(ii);


                }

        });


    }
}