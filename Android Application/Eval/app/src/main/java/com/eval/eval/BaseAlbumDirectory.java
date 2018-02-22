package com.eval.eval;

import android.os.Environment;

import java.io.File;

public class BaseAlbumDirectory {

    private static final String CAMERA_DIR = "/dcim/";

    public File getAlbumStorageDir(String albumName) {
        return new File(
                Environment.getExternalStorageDirectory()
                        + CAMERA_DIR
                        + albumName
        );
    }
}

