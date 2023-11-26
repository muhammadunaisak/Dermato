package com.example.dermato;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
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

public class chatdoctor extends AppCompatActivity implements AdapterView.OnItemClickListener{
    ListView l1;
    SharedPreferences sh;
    String url;

    ArrayList<String> name,did;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chatdoctor);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1=findViewById(R.id.listt);
        url ="http://"+sh.getString("ip", "") + ":5000/viewdoc";
        RequestQueue queue = Volley.newRequestQueue(chatdoctor.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);

                    name= new ArrayList<>();
                    did= new ArrayList<>();

                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        did.add(jo.getString( "lid"));
                        name.add(jo.getString("fname")+" "+jo.getString("lname"));
                    }

                     ArrayAdapter<String> ad=new ArrayAdapter<>(chatdoctor.this,android.R.layout.simple_list_item_1,name);
                    l1.setAdapter(ad);
                    l1.setOnItemClickListener(chatdoctor.this);

//                    l1.setAdapter(new costum3(viewdoctor.this,name,experience,qualification,reg));
//                    l1.setOnItemClickListener(viewdoctor.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(chatdoctor.this, "err"+error, Toast.LENGTH_SHORT).show();
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
    public void onItemClick(AdapterView<?> adapterView, View view, int ik, long l) {
        String ttid=did.get(ik);
        SharedPreferences.Editor edp = sh.edit();
        edp.putString("uid", ttid);
        edp.commit();

        Intent i=new Intent(getApplicationContext(), Test.class);
//        i.putExtra("toid",rid.get(position));

        i.putExtra("name",name.get(ik));


        startActivity(i);

    }
}