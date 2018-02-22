package com.eval.eval;

import android.support.v4.widget.SwipeRefreshLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class WebActivity extends AppCompatActivity {

    WebView webView;
    SwipeRefreshLayout swipeRefreshLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);

        swipeRefreshLayout = (SwipeRefreshLayout) findViewById(R.id.swipe);
        swipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                loadWeb();
            }
        });

        loadWeb();

    }

    public void loadWeb(){

        webView = (WebView) findViewById(R.id.webView);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.getSettings().setAppCacheEnabled(true);
        webView.loadUrl("https://eval-snip.herokuapp.com/python");
        swipeRefreshLayout.setRefreshing(true);
        webView.setWebViewClient(new WebViewClient(){

            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl){
                webView.loadUrl("file:///android_asset/error.html");
                swipeRefreshLayout.setRefreshing(false);

            }

            public void onPageFinished(WebView view,String Url){
                swipeRefreshLayout.setRefreshing(false);
            }
        });
    }

    public void onBackPressed(){

        if(webView.canGoBack()){
            webView.goBack();
        }
        else{
            finish();
        }
    }
}
