package com.example.dermato;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class viewdoctor extends AppCompatActivity implements AdapterView.OnItemClickListener {
ListView l1;
SharedPreferences sh;
String url;
ArrayList<String> reg,name,experience,qualification,did;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewdoctor);

        l1=findViewById(R.id.listview4);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url ="http://"+sh.getString("ip", "") + ":5000/viewdoc";
        RequestQueue queue = Volley.newRequestQueue(viewdoctor.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    reg=new ArrayList<>();
                    name= new ArrayList<>();
                    experience= new ArrayList<>();
                    qualification= new ArrayList<>();
                    did= new ArrayList<>();


                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        reg.add(jo.getString( "regno"));
                        name.add(jo.getString("fname")+" "+jo.getString("lname"));
                        experience.add(jo.getString("experience"));
                        qualification.add(jo.getString("qualification"));
                        did.add(jo.getString("lid"));


                    }

                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new costum3(viewdoctor.this,name,experience,qualification,reg));
                                      l1.setOnItemClickListener(viewdoctor.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(viewdoctor.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();

                return params;
            }
        };
        queue.add(stringRequest);
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        Intent ii=new Intent(getApplicationContext(),Viewschedule.class);
        ii.putExtra("did",did.get(i));
        startActivity(ii);
    }
}